import pandas as pd


def carregar_financial():
    financial = pd.read_csv("df/financial_impact.csv")

    financial["ransom_demanded_usd"] = financial["ransom_demanded_usd"].fillna(0)
    financial["ransom_paid_usd"] = financial["ransom_paid_usd"].fillna(0)
    financial["ransom_source"] = financial["ransom_source"].fillna("none")
    financial["regulatory_fine_usd"] = financial["regulatory_fine_usd"].fillna(0)
    financial["insurance_payout_usd"] = financial["insurance_payout_usd"].fillna(0)
    financial["notes"] = financial["notes"].fillna("")

    financial = financial.drop(columns=["created_at", "updated_at"])

    financial["incident_date"] = pd.to_datetime(
        financial["incident_id"].str[:9].str.replace(
            r"(\d{4}-\d{2})(\d{2})", r"\1-\2", regex=True
        )
    )

    return financial