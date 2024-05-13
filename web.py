import streamlit as st
from hrs_calc import calc_wrkHrs
from proc_Timesheet import proc_Timesheet
def main():
    out_string4 = ""
    st.set_page_config(page_title="This is timesheet application")
    st.title("Timesheet application")

    r1col1, r1col2, r1col3 = st.columns(3)
    r2col1, r2col2 = st.columns(2)
    r3col1, r3col2 = st.columns(2)

    with r1col1:
        l_name = st.text_input("Last Name", placeholder='Doe')
    with r1col2:
        f_name = st.text_input("First Name", placeholder='John')
    with r1col3:
        posn = st.text_input("Position", placeholder='1064')
    with r2col1:
        arrival = st.text_input("Arrived", placeholder='8:00')
    with r2col2:
        depart = st.text_input("Leaving", placeholder='16:30')
    with r3col1:
        lunch_out = st.text_input("Out for Lunch", placeholder='12:00')
    with r3col2:
        lunch_in = st.text_input("In for Lunch", placeholder='13:00')




    if st.button("Process"):
        workHrs, rwwHrs = calc_wrkHrs(arrival, lunch_out, lunch_in, depart)
        out_string = f"Hi {l_name}, {f_name} submitting for {posn}"
        out_string2 = f"Arrive: {arrival} Lunch Out: {lunch_out} Lunch In: {lunch_in} Depart: {depart}"
        out_string3 = f"Total Hours: {workHrs} Rww: {rwwHrs} "
        if rwwHrs < 0:
            out_string4 = f"Hours worked exceeds 8 hrs please revise and submit"
        st.write(out_string)
        st.write(out_string2)
        st.write(out_string3)
        st.write(out_string4)
if __name__ == '__main__':
    main()