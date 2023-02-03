# Homework 6

- [x] Linux Video
- [ ] Real Time Kernel

## Video Response questions 

1. Where does Julia Cartwright work?
National Instruments
2. What is PREEMT_RT? Hint: Google it.
It is a realtime patch for the Linux kernel. It makes the kernel preemptible, which means that the kernel can be interrupted. Used for real time applications where execution time is critical.

3. What is mixed criticality?
It is running code that has need for a realtime os (execution time and when matters alot) and some not as time critical things that a normal linux kernel can handle. Mixed criticality is often done with the combination of a RTOS and a Non Realtime OS on 2 different devices.

4. How can drivers misbehave?
It can misbehave

5. What is Δ in Figure 1?
Time from an event occuring to how fast the OS reponds in a realtime way

6. What is Cyclictest[2]?
Measures difference between the time a task is supposed to wake up and the time it actually wakes up. It is a tool that can be used to measure the latency of the kernel.

7. What is plotted in Figure 2?
Figure 2 is a histogram of the latency of the preempt_rt kernel. It is the time it takes for a thread to sleep vs the expected time it should sleep. It shows both the mainline kernel and the preempt_rt kernel.

8. What is dispatch latency? Scheduling latency?
It is from the time the hardware event fires to the time for the handler thread to be woken up and the thread scheduler to be told to schedule it. The scheduling latency is the time the scheduler takes to schedule it and get it into the cpu for the task to actually be ran.

9. What is mainline?
The mainline is how the cpu switches between threads and what code it is running in what times.

10. What is keeping the External event in Figure 3 from starting?
The code that is executing currently was still running for a while after the external event occured and since it couldn't take control because it is a more important, time constrained task, it had to wait for that code to finish executing.

11. Why can the External event in Figure 4 start sooner? 
The external event can start sooner because the kernel is using the preempt_rt patch. This means that the IRQs only are a small amount of code and that will allow threads to wake up sooner because there is less blocking code.

## Compiling the real time kernel

1. Does the RT kernel have a bounded latency?

2. What are you using to load?

