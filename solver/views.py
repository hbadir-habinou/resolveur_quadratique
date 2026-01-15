from django.shortcuts import render
from django.contrib import messages
import io, base64, matplotlib.pyplot as plt, numpy as np, cmath

def formate(v):
    if abs(v) < 1e-10:
        return "0"
    if v.is_integer():
        return str(int(v))
    return f"{v:.6f}".rstrip("0").rstrip(".")

def home(request):
    context = {}
    error = None

    if request.method == "POST":
        try:
            raw_a = request.POST.get("a", "").strip()
            raw_b = request.POST.get("b", "").strip()
            raw_c = request.POST.get("c", "").strip()

            if not raw_a or not raw_b or not raw_c:
                error = "Tous les champs doivent être remplis."
                raise ValueError

            a = float(raw_a)
            b = float(raw_b)
            c = float(raw_c)

            # Conservation des valeurs saisies
            context["a"] = raw_a
            context["b"] = raw_b
            context["c"] = raw_c

            # Construction propre de l'équation
            terms = []
            if a != 0:
                coef_a = "" if abs(a) == 1 else formate(a)
                terms.append(f"{coef_a}x²" if a > 0 else f"-{coef_a}x²" if a == -1 else f"- {abs(a)}x²")
            if b != 0:
                coef_b = "" if abs(b) == 1 else f" {formate(abs(b))}"
                terms.append(f"+ {coef_b}x" if b > 0 else f"- {coef_b}x")
            if c != 0:
                terms.append(f"+ {formate(c)}" if c > 0 else f"- {formate(abs(c))}")
            if not terms:
                terms = ["0"]
            equation = " ".join(terms).replace("+ -", "- ").strip() + " = 0"
            context["equation"] = equation

            result = []

            if a == 0:
                if b == 0:
                    result.append("Équation indéterminée ou impossible selon la valeur de c.")
                else:
                    x = -c / b
                    result.append(f"Équation linéaire → <strong>x = {formate(x)}</strong>")
            else:
                delta = b**2 - 4*a*c
                result.append(f"Discriminant : \\(\\Delta = {formate(delta)}\\)")

                r1 = (-b + cmath.sqrt(delta)) / (2*a)
                r2 = (-b - cmath.sqrt(delta)) / (2*a)

                if delta > 0:
                    result.append("<strong>Deux racines réelles distinctes :</strong>")
                    result.append(f"\\(x_1 = {formate(r1.real)}\\)")
                    result.append(f"\\(x_2 = {formate(r2.real)}\\)")
                elif delta == 0:
                    result.append("<strong>Racine double :</strong>")
                    result.append(f"\\(x = {formate(r1.real)}\\)")
                else:
                    def fmt_cplx(z):
                        re = formate(z.real)
                        im = formate(abs(z.imag))
                        if im == "1":
                            im_part = "i"
                        else:
                            im_part = f"{im}i"
                        return f"{re} + {im_part}" if z.imag > 0 else f"{re} - {im_part}"
                    result.append("<strong>Racines complexes :</strong>")
                    result.append(f"\\(x_1 = {fmt_cplx(r1)}\\)")
                    result.append(f"\\(x_2 = {fmt_cplx(r2)}\\)")

                # Graphique
                fig, ax = plt.subplots(figsize=(8,6))
                x_vals = np.linspace(-10, 10, 400)
                y_vals = a*x_vals**2 + b*x_vals + c
                ax.plot(x_vals, y_vals, label=f"y = {a}x² + {b}x + {c}", color="#3498db", linewidth=3)
                ax.axhline(0, color='black', lw=1)
                ax.axvline(0, color='black', lw=1)
                ax.grid(True, alpha=0.3)
                ax.set_title("Parabole", fontsize=16)

                if delta >= 0:
                    racines = [r1.real] if delta == 0 else [r1.real, r2.real]
                    for r in racines:
                        ax.plot(r, 0, 'ro', markersize=10)
                        ax.annotate(f"({formate(r)}, 0)", (r, 0), xytext=(0,15),
                                    textcoords="offset points", ha='center', color='red', fontsize=12)

                buf = io.BytesIO()
                plt.savefig(buf, format='png', bbox_inches='tight', dpi=150)
                buf.seek(0)
                context["graph"] = base64.b64encode(buf.read()).decode('utf-8')
                plt.close(fig)

            context["result"] = "<br>".join(result)

        except ValueError:
            if not error:
                error = "Veuillez entrer uniquement des nombres valides dans les champs a, b et c."

    context["error"] = error
    return render(request, "home.html", context)