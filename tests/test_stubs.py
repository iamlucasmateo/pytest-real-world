from unittest.mock import Mock

import pytest

from logic.alarm import Alarm
from logic.sensor import Sensor

class TestAlarm:
    def test_alarm_is_off_by_default(self):
        alarm = Alarm()
        assert not alarm.is_alarm_on
    
    def test_check_too_low_pressure_sounds_alarm(self):
        # using a stub: dependency used only for tests
        alarm = Alarm(sensor=TestSensor())
        alarm.check()
        assert alarm.is_alarm_on
    
    def test_check_too_high_pressure_sounds_alarm(self):
        alarm = Alarm(sensor=TestSensor(30))
        alarm.check()
        assert alarm.is_alarm_on
    
    def test_check_normal_pressure_doesnt_sound_alarm(self):
        alarm = Alarm(sensor=TestSensor(20))
        alarm.check()
        assert not alarm.is_alarm_on
    
    def test_check_pressure_ok_with_mock_stub(self):
        # using Mock for creating stubs 
        # stubs have the same interface but no logic or advanced behavior
        test_sensor = Mock(Sensor)
        test_sensor.sample_pressure.return_value = 18
        alarm = Alarm(test_sensor)
        alarm.check()
        assert not alarm.is_alarm_on

    
class TestSensor:
    def __init__(self, pressure=None):
        self.pressure = pressure or 15
    
    def sample_pressure(self):
        return self.pressure