def calculate_pre_assessment(balance_sheet):
    total_profit = sum(item["profitOrLoss"] for item in balance_sheet)
    average_assets = sum(item["assetsValue"] for item in balance_sheet) / len(
        balance_sheet
    )

    if total_profit > 0 and average_assets > 100000:  # Example threshold
        return 100
    elif total_profit > 0:
        return 60
    else:
        return 20


def summarize_balance_sheet(balance_sheet):
    total_profit_loss = sum(item["profitOrLoss"] for item in balance_sheet)
    average_assets_value = sum(item["assetsValue"] for item in balance_sheet) / len(
        balance_sheet
    )
    return {
        "totalProfitOrLoss": total_profit_loss,
        "averageAssetsValue": average_assets_value,
    }
