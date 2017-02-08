from pynvml import *
from prometheus_client import Gauge

from .metric import *

def build_metrics():
    metrics = [
        TemperatureMetric(), ShutdownTemperatureMetric(), SlowdownTemperatureMetric(), FanSpeedMetric(),
        TotalMemoryMetric(), FreeMemoryMetric(), UsedMemoryMetric(),
        GPUUtilizationMetric(), MemoryUtilizationMetric(),
        PowerUsageMetric(), PowerManagementLimitMetric(),
        #ECCDoubleBitErrorsMetric(), ECCSingleBitErrorsMetric(),
        ProcessCountMetric()
    ]

    device_count = int(nvmlDeviceGetCount())
    driver_version = nvmlSystemGetDriverVersion()

    device_count_metric = Gauge('nvidia_device_count', 'Number of compute devices in the system', [DRIVER_VERSION_LABEL])
    device_count_metric.labels(driver_version).set_function(lambda: int(nvmlDeviceGetCount())) # Could change if a GPU dies

    for device_index in range(device_count):
        handle = nvmlDeviceGetHandleByIndex(device_index)
        name = nvmlDeviceGetName(handle)
	
	metrics[0].promethus_metric.labels(device_index, name, driver_version).set_function(lambda: metrics[0].collect(handle))
	metrics[1].promethus_metric.labels(device_index, name, driver_version).set_function(lambda: metrics[1].collect(handle))
	metrics[2].promethus_metric.labels(device_index, name, driver_version).set_function(lambda: metrics[2].collect(handle))
	metrics[3].promethus_metric.labels(device_index, name, driver_version).set_function(lambda: metrics[3].collect(handle))
	metrics[4].promethus_metric.labels(device_index, name, driver_version).set_function(lambda: metrics[4].collect(handle))
	metrics[5].promethus_metric.labels(device_index, name, driver_version).set_function(lambda: metrics[5].collect(handle))
	metrics[6].promethus_metric.labels(device_index, name, driver_version).set_function(lambda: metrics[6].collect(handle))
	metrics[7].promethus_metric.labels(device_index, name, driver_version).set_function(lambda: metrics[7].collect(handle))
	metrics[8].promethus_metric.labels(device_index, name, driver_version).set_function(lambda: metrics[8].collect(handle))
	metrics[9].promethus_metric.labels(device_index, name, driver_version).set_function(lambda: metrics[9].collect(handle))
	metrics[10].promethus_metric.labels(device_index, name, driver_version).set_function(lambda: metrics[10].collect(handle))
	metrics[11].promethus_metric.labels(device_index, name, driver_version).set_function(lambda: metrics[11].collect(handle))
#	metrics[12].promethus_metric.labels(device_index, name, driver_version).set_function(lambda: metrics[12].collect(handle))
#	metrics[13].promethus_metric.labels(device_index, name, driver_version).set_function(lambda: metrics[13].collect(handle))

#	ITS FACKING NOT WORK WITH FOR!!!!!
#        for metric in metrics:
#            metric.promethus_metric.labels(device_index, name, driver_version).set_function(lambda: metric.collect(handle))

