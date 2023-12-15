"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.
 
    :param temperature: int or float - temperature value in kelvin.
    :param neutrons_emitted: int or float - number of neutrons emitted per second.
    :return: bool - is criticality balanced?

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800 K.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """
    temp_value = False 
    if temperature < 800 and neutrons_emitted > 500 and (temperature*neutrons_emitted)<500000:
        temp_value = True
    return temp_value


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    :param voltage: int or float - voltage value.
    :param current: int or float - current value.
    :param theoretical_max_power: int or float - power that corresponds to a 100% efficiency.
    :return: str - one of ('green', 'orange', 'red', or 'black').

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """
    var_color = ""
    generated_power = voltage * current
    percent = (generated_power/theoretical_max_power )*100 
    
    if percent >= 80 :
        var_color = "green"
    if 60 <=  percent < 80:
        var_color = "orange"
    if 30 <= percent < 60:
        var_color = "red"
    if percent < 30:
        var_color = "black"
    return var_color


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.

    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').

    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """
    var_status = ""
    var_thres_ninety = threshold * 0.9
    var_thres_ten = threshold * 0.1
    var_tem_neu = temperature * neutrons_produced_per_second
    if var_tem_neu < var_thres_ninety:
        var_status = "LOW"
    elif (threshold-var_thres_ten) < var_tem_neu < (threshold+var_thres_ten) :
        var_status = "NORMAL"
    else:
        var_status = "DANGER"
    return var_status