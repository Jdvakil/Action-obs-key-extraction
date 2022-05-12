#!/usr/bin/env python3
import numpy as np

py_dict = {
            'qpos': np.random.randint(100, size=(9,30)),
            'qvel': np.random.randint(100, size=(9,12)),
            'etc': np.random.randint(100,size=(1,1)),
            'a': np.random.randint(100, size=(2,2)),
            'b': np.random.randint(100, size=(2,1))
          }
in_action = ['qpos', 'qvel', 'etc']
in_obs = ['qpos', 'a']


def numAlg(in_action, in_obs, py_dict):
    out_action_temp = []
    out_obs_temp = []

    for key in in_action:
        for dict_key in py_dict:
            if(key == dict_key):
                for arr in py_dict[key]:
                    for val in arr:
                        out_action_temp.append(val)
    
    for key in in_obs:
        for dict_key in py_dict:
            if(key == dict_key):
                for arr in py_dict[key]:
                    for val in arr:
                        out_obs_temp.append(val)
    out_action = np.array(out_action_temp)
    out_obs = np.array(out_obs_temp)
                        
    return out_action, out_obs

def main():
    out_a, out_o = numAlg(in_action, in_obs, py_dict)
    print(py_dict)
    print("###############################")
    print(out_a)
    print("###############################")
    print(out_o.shape)
    
if __name__=="__main__":
    main()
