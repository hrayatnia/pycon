from brian import *
from numpy import *

if __name__ == '__main__':
	N = 1 # number of neurons

	tau_m = 10 * ms # membrane time constant
	v_r = 0 * mV # reset potential
	v_th = 15 * mV # threshold potential
	I_c = 20 * mV # constant input current

	eqs = '''
	dv/dt = -(v-I)/tau_m : volt
	I : volt
	'''

	lif = NeuronGroup(N, model=eqs, threshold=v_th, reset=v_r)
	# You can add randomness in initial membrane potential by changing the following line
	lif.v = v_r * mV + 0 * mV * rand(len(lif))
	lif.I = I_c

	spikes = SpikeMonitor(lif)
	v_trace = StateMonitor(lif, 'v', record=True)

	run(0.1*second)

	figure(1)
	plot(v_trace.times/ms,v_trace[0]/mV)
	xlabel('Time (ms)', fontsize=24)