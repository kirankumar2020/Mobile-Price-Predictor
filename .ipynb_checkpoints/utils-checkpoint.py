import pickle
import numpy as np


def get_predicted_price_class(battery_power, blue, clock_speed, dual_sim, fc, four_g, int_memory, m_dep,mobile_wt,n_cores,pc,px_height,px_width,ram,sc_h,sc_w,talk_time,three_g,touch_screen,wifi):
    mobile_path = r"C:\Users\kiran\OneDrive\Desktop\PDS\01-Class-Notes\PRACTICED\Flask\Mobile_phone\MobilePhone....KNN_clf_model.pkl"
    
    with open(mobile_path, 'rb') as f:
        model = pickle.load(f)
        
        
        
        test_array = np.array([battery_power, blue, clock_speed, dual_sim, fc, four_g, int_memory, m_dep,mobile_wt,n_cores,pc,px_height,px_width,ram,sc_h,
                     sc_w,talk_time,three_g,touch_screen,wifi], ndmin = 2)
        # print(test_array)
        predicted_price_class = model.predict(test_array)[0]
        print("predicted_price_class :",predicted_price_class)
        
        
        
        return predicted_price_class