# Homework 2

- [x] Buttons and Leds
- [x] Measuring a GPIO ping on Oscilloscope
- [x] GPIOd
- [ ] getSetEvent.py
- [x] Security
- [x] Etch-e-sketch

## Measuring a gpio pin on an Oscilloscope

```bash
bone$ cd exercises/gpio
bone$ ./togglegpio.sh 44 0.1 
```

1. What's the min and max voltage?
**Max of 2.238V and min of 58.91mV**

2. What period and frequency is it?
**238.9ms and 4.185Hz**

3. How close is it to 100ms?
**It is about (238.9 ms / 2) - 100ms = 19.45ms off**

4. Why do they differ?
**Because there are instructions that are being ran by bash that are in between toggling to open the file and write to it. This is why the period is not exactly 100ms. Bash is not really that fast and so that is why there is so much time is because it opens the file and writes to it each loop.**

5. Run htop and see how much processor you are using.
**About 3-4% of the processor is being used.**

6. Try different values for the sleep time (2nd argument). What's the shortest period you can get? Make a table of the fastest values you try and the corresponding period and processor usage. Try using markdown tables: https://www.markdownguide.org/extended-syntax/#tables

| Sleep time | Period |
|------|--------|
| 0.1 | 238.9ms |
| 0.098 | 234.3ms |
| 0.080 | 199.6 |

7. How stable is the period?
**Kinda unstable because the standard deviation is 87.86m**

8. Try launching something like vi. How stable is the period?
**Kinda unstable as well, didn't notice much of a difference and the std dev is actually lower**

9. Try cleaning up togglegpio.sh and removing unneeded lines. Does it impact the period?
**Removing unnecessary lines does I think make the period smaller, but it is hard to tell really**

10. Togglegpio.sh uses bash (first line in file). Try using sh. Is the period shorter?
**It is a lot shorter, so sh runs faster than bash.**

11. What's the shortest period you can get? 

### Results

| Name | Period | Frequency |
|------|--------|-----------|
| Shell Script | 238.9ms | 4.185Hz |
| Python Script| 9.902ms | 101.02Hz |
| C program w/ lseek | 0.0752ms | 13.3kHz |

### Change SSH Port

I have in fact changed my ssh port to 2022

# hw02 grading

| Points      | Description |
| ----------- | ----------- |
|  2/2 | Buttons and LEDs 
|  8/8 | Etch-a-Sketch works
|      | Measuring a gpio pin on an Oscilloscope 
|  2/2 | Questions answered
|  4/4 | Table complete
|  2/2 | gpiod
|      | Security
|  1/1 | ssh port 
|  0/1 | fail2ban
| 20/20   | **Total**
+1 for aggrator.

Nice check list at the start.
Max voltage seems too small.

It suprising the shell script is so fast.

Looks like you got the gpiod aggregator going.  Nice script.