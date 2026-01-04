import pandas as pd
import datetime

# --- CONFIGURATION ---
BASE_PREMIUM = 2000  # Starting price
CRITICAL_COST = 5000 # Add this much for every Critical vul
HIGH_COST = 2000     # Add this much for every High vul
MEDIUM_COST = 500    # Add this much for every Medium vul
DEFENDER_DISCOUNT = 0.20 # 20% off if Defender is active

def calculate_premium(csv_file, has_defender=False):
    print(f"--- ANALYZING: {csv_file} ---")
    try:
        df = pd.read_csv(csv_file)
        criticals = df[df['Risk'] == 'Critical'].shape[0]
        highs = df[df['Risk'] == 'High'].shape[0]
        mediums = df[df['Risk'] == 'Medium'].shape[0]
        
        print(f"Findings: {criticals} Critical | {highs} High | {mediums} Medium")
        
        risk_penalty = (criticals * CRITICAL_COST) + (highs * HIGH_COST) + (mediums * MEDIUM_COST)
        total_premium = BASE_PREMIUM + risk_penalty
        
        if has_defender:
            print("✅ DISCOUNT APPLIED: Microsoft Defender Detected")
            discount_amount = total_premium * DEFENDER_DISCOUNT
            total_premium = total_premium - discount_amount
        else:
            print("❌ PENALTY: No EDR/Defender Detected")
            
        return total_premium, criticals, highs
        
    except FileNotFoundError:
        print("Error: CSV file not found.")
        return 0, 0, 0

# --- CLI INTERFACE ---
if __name__ == "__main__":
    print("🛡️  SHIELDRATE: AUTOMATED UNDERWRITING ENGINE 🛡️")
    filename = input("Enter the Tenable CSV filename: ")
    defender_status = input("Is Microsoft Defender active? (yes/no): ").lower()
    has_defender = True if defender_status == 'yes' else False

    premium, crit, high = calculate_premium(filename, has_defender)
    
    print(f"\n💰 FINAL PREMIUM: ${premium:,.2f}")
    if premium > 10000:
        print("⚠️  STATUS: HIGH RISK - DECLINE")
    else:
        print("✅  STATUS: APPROVED")
