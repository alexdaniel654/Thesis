import numpy as np
import nibabel as nib
from dipy.tracking.eudx import EuDX
from dipy.tracking import utils
from dipy.tracking.streamline import Streamlines
from dipy.reconst import peaks
from dipy.reconst.csdeconv import ConstrainedSphericalDeconvModel, recursive_response
from dipy.core.gradients import gradient_table_from_bvals_bvecs
from dipy.io.streamline import save_trk

if __name__ == '__main__':
	print('Ingesting Data')
	img = nib.load('data.nii.gz')
	mask = nib.load('mask.nii.gz')
	bvals = np.loadtxt('bvals')
	bvecs = np.loadtxt('bvecs')
	data = img.get_fdata()
	
	mask_data = mask.get_fdata()
	mask_data = (mask_data>0)
	
	gtab = gradient_table_from_bvals_bvecs(bvals.T, bvecs.T)
	
	print('Estimating Fibre Response Function')
	response = recursive_response(gtab, data, 
								  mask=mask_data, sh_order=8,
								  peak_thr=0.01, init_fa=0.08,
								  init_trace=0.0021, iter=8, 
								  convergence=0.001, parallel=False)
	
	print('Generating CSD Model')
	csd_model = ConstrainedSphericalDeconvModel(gtab, response, 
												sh_order=6)
	
	print('Getting Peaks From Model')
	csd_peaks = peaks.peaks_from_model(model=csd_model,
									   data=data,
									   sphere=peaks.default_sphere,
									   relative_peak_threshold=.8,
									   min_separation_angle=45,
									   mask=mask_data)
	
	print('Generating Seeds')
	seeds = utils.seeds_from_mask(mask_data, density=1)
	
	print('Propogating From Seeds')
	streamline_gen = EuDX(csd_peaks.peak_values, 
						  csd_peaks.peak_indices,
						  odf_vertices=peaks.default_sphere.vertices,
						  a_low=.05, step_sz=.5, seeds=seeds)
	
	print('Generating Streamlines')
	streamlines = Streamlines(streamline_gen, buffer_size=512)
	
	print('Saving Output For Your Perusal')
	save_trk('tracts.trk', streamlines, 
			 shape=mask.shape, vox_size=data.header.get_zooms(), 
			 affine=data.affine)