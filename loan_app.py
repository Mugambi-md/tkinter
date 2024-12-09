from datetime import datetime, date

def loan_arrears(principal, period, rate, s_period, p_bal, i_bal):
   

    def principal_arrears(principal, period, s_period, p_bal):
         principal_payment = principal/period
         principal_to_pay = principal_payment*s_period
         remaining_principal = principal_to_pay-principal
         arrears = remaining_principal+p_bal
         return arrears
    
    principal_arrears = principal_arrears(principal, period, s_period, p_bal)

    def averange_interest(principal, period, rate, s_period):
         principal_payment = principal/period
         av_int = (principal_payment*rate*(period+1))/200
         total_av_int = av_int*s_period
         return total_av_int
    
    total_averange_interest = averange_interest(principal, period, rate, s_period)

    def paid_interest(principal, rate, s_period, i_bal):
         principal_payment = principal/period
         principal = principal
         cumulative_interest = 0

         for months in range(1, s_period+1):
              interest_for_month = (rate/100)*principal
              principal -= principal_payment
              cumulative_interest += interest_for_month
              paid_interest = cumulative_interest - i_bal
              return paid_interest
         
    paid_interest = paid_interest(principal, rate, s_period, i_bal)
    interest_arrears = total_averange_interest-paid_interest

    return f"Principal arrears: {principal_arrears:.2f}. Interest arrears: {interest_arrears:.2f}"

def months_difference(selected_year, selected_month, selected_day):
    
    selected_date = date(selected_year, selected_month, selected_day)
    today = date.today()
    month_difference = (today.year - selected_date.year)*12 + today.month - selected_date.month
    if today.day<selected_date.day:
        month_difference-=1
     
    return month_difference
