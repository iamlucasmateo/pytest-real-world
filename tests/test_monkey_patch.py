from unittest.mock import Mock, patch

from logic.alarm import Alarm

class TestAlarm():
    # with context manager
    def test_check_with_too_high_pressure(self):
        with patch("logic.alarm.Sensor") as test_sensor_class:
            test_sensor_instance = Mock()
            test_sensor_instance.sample_pressure.return_value = 22
            test_sensor_class.return_value=test_sensor_instance
            alarm = Alarm()
            alarm.check()
            assert alarm.is_alarm_on

    # with patch
    @patch("logic.alarm.Sensor")
    def test_check_with_too_low_pressure(self, test_sensor_class):
        test_sensor_instance = Mock()
        test_sensor_instance.sample_pressure.return_value = 15
        test_sensor_class.return_value = test_sensor_instance
        alarm = Alarm()
        alarm.check()
        assert alarm.is_alarm_on