#include <linux/module.h>
#define INCLUDE_VERMAGIC
#include <linux/build-salt.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

BUILD_SALT;

MODULE_INFO(vermagic, VERMAGIC_STRING);
MODULE_INFO(name, KBUILD_MODNAME);

__visible struct module __this_module
__section(".gnu.linkonce.this_module") = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};

#ifdef CONFIG_RETPOLINE
MODULE_INFO(retpoline, "Y");
#endif

static const struct modversion_info ____versions[]
__used __section("__versions") = {
	{ 0x5d0b370a, "module_layout" },
	{ 0xfe990052, "gpio_free" },
	{ 0xc1514a3b, "free_irq" },
	{ 0x92d5838e, "request_threaded_irq" },
	{ 0xdd412ce6, "gpiod_to_irq" },
	{ 0x79b51d76, "gpiod_set_debounce" },
	{ 0xb70716cc, "gpiod_direction_input" },
	{ 0x872f0374, "gpiod_direction_output_raw" },
	{ 0x47229b5c, "gpio_request" },
	{ 0xc5850110, "printk" },
	{ 0x8b252912, "gpiod_set_raw_value" },
	{ 0xfd94ff5d, "gpiod_export" },
	{ 0xc1366aa3, "gpiod_unexport" },
	{ 0xefd6cf06, "__aeabi_unwind_cpp_pr0" },
	{ 0x34af7d78, "gpiod_get_raw_value" },
	{ 0x436f788e, "gpio_to_desc" },
};

MODULE_INFO(depends, "");


MODULE_INFO(srcversion, "97763CAD891F4E35BC7D9BE");
