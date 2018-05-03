from pydap.client import open_url

dataset = open_url('http://test.opendap.org/dap/data/nc/coads_climatology.nc')
var = dataset['SST']
print(var.shape)
print(var.dtype)
data = var[0,10:14,10:14]
print(data)
print(data.data)