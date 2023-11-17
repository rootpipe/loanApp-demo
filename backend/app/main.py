from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/submit-application", methods=["POST"])
def submit_application():
    try:
        data = request.json
        business_name = data["businessName"]
        year_established = data["yearEstablished"]
        balance_sheet = data["balanceSheet"]

        pre_assessment = calculate_pre_assessment(balance_sheet)
        balance_sheet_summary = summarize_balance_sheet(balance_sheet)

        response = {
            "balance_sheet_summary": balance_sheet_summary,
            "pre_assessment": pre_assessment,
        }
    except KeyError as e:
        response = {"status": "error", "message": f"Missing field: {str(e)}"}
    except Exception as e:
        response = {"status": "error", "message": str(e)}

    return jsonify(response)


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


if __name__ == "__main__":
    app.run(debug=True)
