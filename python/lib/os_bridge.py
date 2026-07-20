# type: ignore
import avocet_core
import avocet_sys

class OSBridge:
    @staticmethod
    def get_system_telemetry():
        return {
            "version": avocet_sys.get_kernel_version(),
            "vendor": avocet_sys.get_cpu_vendor(),
            "memory_total_mb": avocet_sys.get_total_memory() // 1024,
            "uptime_ticks": avocet_core.get_ticks()
        }

    @staticmethod
    def process_yield(ticks=10):
        avocet_core.sleep(ticks)

    @staticmethod
    def capture_input():
        return avocet_core.getc()

    @staticmethod
    def emit_log(message):
        avocet_core.kprint(f"[OS_BRIDGE] {message}\n")

    @staticmethod
    def trigger_power_state(action):
        if action == "reboot":
            avocet_sys.reboot()
        elif action == "shutdown":
            avocet_sys.shutdown()
