import mne  
raw = mne.io.read_raw_fif('raw.fif', preload=True)  # load data  
raw.info['bads'] = ['MEG 2443', 'EEG 053']  # mark bad channels  
raw.filter(l_freq=None, h_freq=40.0)  # low-pass filter data  
# Extract epochs and save them:
picks = mne.pick_types(raw.info, meg=True, eeg=True, eog=True,  
                       exclude='bads')  
events = mne.find_events(raw)  
reject = dict(grad=4000e-13, mag=4e-12, eog=150e-6)  
epochs = mne.Epochs(raw, events, event_id=1, tmin=-0.2, tmax=0.5,  
                    proj=True, picks=picks, baseline=(None, 0),  
                    preload=True, reject=reject)  
# Compute evoked response and noise covariance
evoked = epochs.average()  
cov = mne.compute_covariance(epochs, tmax=0)  
evoked.plot()  # plot evoked  
# Compute inverse operator:
fwd_fname = 'sample_audvis−meg−eeg−oct−6−fwd.fif'  
fwd = mne.read_forward_solution(fwd_fname, surf_ori=True)  
inv = mne.minimum_norm.make_inverse_operator(raw.info, fwd,  
                                             cov, loose=0.2)  
# Compute inverse solution:
stc = mne.minimum_norm.apply_inverse(evoked, inv, lambda2=1./9.,  
                                     method='dSPM')  
# Morph it to average brain for group study and plot it
stc_avg = mne.morph_data('sample', 'fsaverage', stc, 5, smooth=5)  
stc_avg.plot()