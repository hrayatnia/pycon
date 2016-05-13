
import os.path as op

import mne

data_path = op.join(mne.datasets.sample.data_path(), 'MEG', 'sample')
raw = mne.io.read_raw_fif(op.join(data_path, 'sample_audvis_raw.fif'))
events = mne.read_events(op.join(data_path, 'sample_audvis_raw-eve.fif'))


raw.plot(block=True, events=events)


raw.plot_sensors(kind='3d', ch_type='mag')


projs = mne.read_proj(op.join(data_path, 'sample_audvis_eog-proj.fif'))
raw.add_proj(projs)
raw.plot_projs_topomap()


raw.plot()


raw.plot_psd()


layout = mne.channels.read_layout('Vectorview-mag')
layout.plot()
raw.plot_psd_topo(tmax=30., fmin=5., fmax=60., n_fft=1024, layout=layout)
