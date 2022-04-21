import numpy as np
import requests
import json

class MkvClient:

  def __init__(self, app):
    self.table = {}
    self.app = app
    self.mkv_url = "http://localhost:8765"

  def Put(self, k, m, ttl=60):
    #print("Mkv-Put: %s\n" % k)
    self.table[self.GenFullKey(k)] = m
    MKV_PUT = self.mkv_url + "/Put"
    param = {}
    vals = []
    for v in np.array(m).ravel():
       vals.append(v)
    param["Key"] = self.GenFullKey(k)
    param["Row"] = len(m)
    param["Col"] = len(m[0])
    param["Vals"] = vals
    print(param["Vals"])
    print(param)
    h = {'Content-Type': 'application/json'}
    response = requests.put(MKV_PUT, headers=h, data=json.dumps(param))
    if response.status_code != 202:
      print("%s response with error code %s" % (MKV_PUT, response.status_code))
    return
  
  def Get(self, k):
    #print("Mkv-Get: %s\n" % k)
    MKV_GET = self.mkv_url + "/Get"
    param = {}
    param["Key"] = self.GenFullKey(k)
    h = {'Content-Type': 'application/json'}
    response = requests.get(MKV_GET, headers=h, data=json.dumps(param))
    if response.status_code != 200:
      print("%s response with error code %s" % (MKV_GET, response.status_code)) 
    m = response.json() 
    return np.array(m["Value"] ).reshape(m["Row"], m["Col"])
  
  def Mul(self, k0, k1, ttl=60):
    #print("Mkv-Mul: %s * %s\n" % (k0, k1))
    #print(self.table)
    #m0 = self.table[fk0]
    #m1 = self.table[fk1]
    #r = np.dot(m0, m1)
    #self.table[self.GenFullKey(k0 + "MUL" + k1)] = r
    MKV_MUL = self.mkv_url + "/Mul"
    param = {}
    param["Key0"] = self.GenFullKey(k0)
    param["Key1"] = self.GenFullKey(k1)
    h = {'Content-Type': 'application/json'}
    response = requests.get(MKV_MUL, headers=h, data=json.dumps(param))
    if response.status_code != 200:
      print("%s response with error code %s" % (MKV_MUL, response.status_code))
    m = response.json() 
    return np.array(m["Value"] ).reshape(m["Row"], m["Col"])

  def GenFullKey(self, k):
    return self.app + "-" + k

MKV = MkvClient("RNNLM")


if __name__ == "__main__":
  MKV.Put("m1", [[1.2,2.2],[4.3,5.4],[3.3,6.1]])
  print(MKV.Mul("m0", "m1"))
  #MKV.Get("m0")

