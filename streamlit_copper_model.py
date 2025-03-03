# streamlit copper model prediction

"""
This is the user interface of model prediction and this will use the pretrained *.pkl file to store the data.
"""
import numpy as np
from model_function import *
import warnings

warnings.filterwarnings("ignore")

st.set_page_config(page_title="Industrial Copper Modeling",
                   page_icon=":factory:",
                   layout="wide",
                   menu_items={
                       "About": """
                        **Industrial Copper Modeling**  
                        This is a machine learning model created with **Python** and **Scikit-learn**,  
                        along with other supporting models. UI is built using **Streamlit**.
                
                        **👨‍💻 Developer:** [Elamparithi](https://www.linkedin.com/in/elamparithi-t/)  
                        **📂 GitHub Repository:** [Industrial Copper Modeling](https://github.com/Elam-parithi/Industrial-Copper-Modeling)  
                        """
                        }
                   )

st.header(":factory: :green[Industrial] :orange[copper] :violet[model]",
          anchor=False, divider=None)
st.html('Created by <b><a href="https://www.linkedin.com/in/elamparithi-t/" target="_blank">Elamparithi</a></b>')
st.write('')
tab1, tab2 = st.tabs(["Sale price prediction", "Status prediction"])
with tab1:
    # Define the widgets for user input
    with st.form("my_form"):
        col1, col2, col3 = st.columns([5, 2, 5])
        with col1:
            price_status = st.selectbox("Status", status_options, key=1)
            price_item_type = st.selectbox("Item Type", item_type_options, key=2)
            price_country = st.selectbox("Country", sorted(country_options), key=3)
            price_application = st.selectbox("Application", sorted(application_options), key=4)
            price_product_ref = st.selectbox("Product Reference", product, key=5)
        with col3:
            quantity_tons = st.text_input("Enter Quantity Tons:  [ 611728 - 1722207579 ]")
            thickness = st.text_input("Enter thickness:  [ 0.18 - 400 ]")
            width = st.text_input("Enter width:   [ 1 - 2990 ]")
            customer = st.text_input("customer ID:   [ 12458 - 30408185 ]")
            submit_button = st.form_submit_button(label="PREDICT PRICE")

        price_vars = [quantity_tons, thickness, width, customer]
    if input_validation(submit_button, price_vars):
        price_model, price_scaler, price_transformer, s_loaded = load_model_artifacts(price_artifacts)

        new_sample = np.array([[np.log(float(quantity_tons)), price_application, np.log(float(thickness)), float(width),
                                price_country, float(customer), int(price_product_ref), price_item_type, price_status]])
        new_sample_ohe = price_transformer.transform(new_sample[:, [7]]).toarray()
        new_sample_be = s_loaded.transform(new_sample[:, [8]]).toarray()
        new_sample = np.hstack((new_sample[:, [0, 1, 2, 3, 4, 5, 6, ]], new_sample_ohe, new_sample_be))
        new_sample1 = price_scaler.transform(new_sample)
        predicted_price = price_model.predict(new_sample1)[0]
        st.write('## :green[Predicted selling price:] ', np.exp(predicted_price))

with tab2:
    with st.form("my_form1"):
        col1, col2, col3 = st.columns([5, 1, 5])

        with col1:
            status_quantity = st.text_input("Enter Quantity Tons (Min:611728 & Max:1722207579)")
            status_thickness = st.text_input("Enter thickness (Min:0.18 & Max:400)")
            status_width = st.text_input("Enter width (Min:1, Max:2990)")
            status_customer = st.text_input("customer ID (Min:12458, Max:30408185)")
            status_selling = st.text_input("Selling Price (Min:1, Max:100001015)")

        with col3:
            status_item_type = st.selectbox("Item Type", item_type_options, key=21)
            status_country = st.selectbox("Country", sorted(country_options), key=31)
            status_application = st.selectbox("Application", sorted(application_options), key=41)
            status_product_ref = st.selectbox("Product Reference", product, key=51)
            status_submit = st.form_submit_button(label="PREDICT")

        status_vars = [status_quantity, status_thickness, status_width, status_customer, status_selling]

    if input_validation(status_submit, status_vars):
        status_loaded_model, status_scaler_loaded, Item_encode = load_model_artifacts(status_artifacts)

        new_sample = np.array([[np.log(float(status_quantity)),
                                np.log(float(status_selling)), status_application,
                                np.log(float(status_thickness)),
                                float(status_width), status_country,
                                int(status_customer),
                                int(status_product_ref),
                                status_item_type]])

        new_sample_ohe = Item_encode.transform(new_sample[:, [8]]).toarray()
        new_sample = np.hstack((new_sample[:, [0, 1, 2, 3, 4, 5, 6, 7]], new_sample_ohe))
        new_sample = status_scaler_loaded.transform(new_sample)
        predicated_status = status_loaded_model.predict(new_sample)
        if predicated_status == 1:
            st.write('## :green[✌️The Status is Won] ')
        else:
            st.write('## :red[👎 The status is Lost] ')
