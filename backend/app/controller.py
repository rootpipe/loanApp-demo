from flask_cors import cross_origin
from . import app
from flask import request, jsonify
from app.services import calculate_pre_assessment, summarize_balance_sheet


@app.route("/submit-application", methods=["POST"])
@cross_origin()
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
