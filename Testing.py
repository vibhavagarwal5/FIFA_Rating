
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import pickle
from sklearn.metrics import mean_squared_error


# In[3]:


model = pickle.load(open('./Pickle models/MultiOutputRegressor_GradientBoostingRegressor1.p','rb'))


# In[4]:


test = pd.read_csv('test.csv')


# In[5]:


# Define the target feature set for the problem
y_features = ["overall", "rs", "rw", "rf", "ram", "rcm", "rm", "rdm", "rcb", "rb", "rwb", "st", "lw", "cf", "cam", "cm", "lm", "cdm", "cb", "lb", "lwb", "ls", "lf", "lam", "lcm", "ldm", "lcb"]


# In[6]:


# Aggregate feature set
features = ["club_le", "real_face", "age", "league_le", "height_cm", "weight_kg", "body_type_le", "nationality_le", "eur_value", "eur_wage", "potential", "pac", "sho", "pas", "dri", "def", "phy", "international_reputation", "skill_moves"]


# In[7]:



Ytest_ = test[y_features]
Xtest_ = test[features]


# In[8]:


model.score(Xtest_, Ytest_)


# In[9]:


mean_squared_error(Ytest_, model.predict(Xtest_))

