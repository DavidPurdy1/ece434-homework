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
	{ 0x5994ba2b, "param_ops_uint" },
	{ 0xfe990052, "gpio_free" },
	{ 0xc1366aa3, "gpiod_unexport" },
	{ 0x60e24f6d, "kthread_stop" },
	{ 0x3caf1e7c, "wake_up_process" },
	{ 0xcd23bb4c, "kthread_create_on_node" },
	{ 0xfd94ff5d, "gpiod_export" },
	{ 0x872f0374, "gpiod_direction_output_raw" },
	{ 0x47229b5c, "gpio_request" },
	{ 0x56c87b84, "kobject_put" },
	{ 0x4792735b, "sysfs_create_group" },
	{ 0x868f8b1f, "kobject_create_and_add" },
	{ 0xf21c1e9a, "kernel_kobj" },
	{ 0x8f678b07, "__stack_chk_guard" },
	{ 0x86332725, "__stack_chk_fail" },
	{ 0xbcab6ee6, "sscanf" },
	{ 0x84b183ae, "strncmp" },
	{ 0xf9a482f9, "msleep" },
	{ 0xb3f7646e, "kthread_should_stop" },
	{ 0xc5850110, "printk" },
	{ 0x8b252912, "gpiod_set_raw_value" },
	{ 0x436f788e, "gpio_to_desc" },
	{ 0x3c3ff9fd, "sprintf" },
	{ 0xefd6cf06, "__aeabi_unwind_cpp_pr0" },
};

MODULE_INFO(depends, "");


MODULE_INFO(srcversion, "9DE81B406D56B5BE8F06ED5");
