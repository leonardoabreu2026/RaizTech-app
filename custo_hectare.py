# RaizTech - modulo de custo por hectare
# Calcula quanto cada talhao custou em insumos na safra

def custo_por_hectare(custo_total_insumos, area_hectares):
    if area_hectares <= 0:
        raise ValueError("A area do talhao precisa ser maior que zero")
    return round(custo_total_insumos / area_hectares, 2)


if __name__ == "__main__":
    print("Custo por hectare: R$", custo_por_hectare(18750, 12.5))
