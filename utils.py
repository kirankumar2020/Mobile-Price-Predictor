import pickle
import numpy as np


def get_predicted_price_class(battery_power, blue, clock_speed, dual_sim, fc, four_g, int_memory, m_dep,mobile_wt,n_cores,pc,px_height,px_width,ram,sc_h,sc_w,talk_time,three_g,touch_screen,wifi):
    mobile_path = r"MobilePhone....KNN_clf_model.pkl"
    
    with open(mobile_path, 'rb') as f:
        model = pickle.load(f)
        
        
        
        test_array = np.array([battery_power, blue, clock_speed, dual_sim, fc, four_g, int_memory, m_dep,mobile_wt,n_cores,pc,px_height,px_width,ram,sc_h,
                     sc_w,talk_time,three_g,touch_screen,wifi], ndmin = 2)
        # print(test_array)
        predicted_price_class = model.predict(test_array)[0]
        print("predicted_price_class :",predicted_price_class)
        if predicted_price_class == 3:
            price = "30-35k"
        elif predicted_price_class == 2:
            price = "25-30k"
        elif predicted_price_class == 1:
            price = "18-24k"
        else:
            price = "10-16k"
        print("Mobile price: ", price)
        
        
        # price = {0: '10-16k', 1: '18-24k', 2: '25-30k', 3: '30-35k'}
        return price