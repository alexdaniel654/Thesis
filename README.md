# Developing Techniques for Quantitative Renal Magnetic Resonance Imaging
## PhD Thesis - Alex Daniel

### Abstract

The kidneys are morphologically and functionally complex organs and as such, lend themselves to complex methodologies of study. One such methodology is quantitative Magnetic Resonance Imaging (MRI). Rather than simply taking a structural image of the kidneys, quantitative MRI aims to measure physical properties such as the rate of blood flow, tissue perfusion, oxygen consumption and more fundamental properties of the matter making up the organ such as its proton density or longitudinal relaxation time, T1 and transverse relaxation time T2. This is done without the need for ionising radiation and often without exogenous contrast agents, thus making MRI an ideal tool for both clinical and research use.
	
Multiple methods have been developed to measure the transverse relaxation time, T2, of the kidneys, often leading to inconsistent results between studies. Here, a methodical comparison of four prominent techniques is performed. This comparison makes use of quantitative phantoms before proceeding to assess each technique in-vivo in healthy volunteers. A Gradient Spin Echo (GraSE) sequence is recommended for future renal T2 mapping.

Techniques to measure the Renal Metabolic Rate of Oxygen (RMRO2) would be highly desirable. Susceptibility Based Oximetry (SBO) and T2 Relaxation Under Spin Tagging (TRUST) are modified for use in the abdomen. SBO is found to be poorly suited to measuring oxygenation in the renal veins, however TRUST is used to successfully measure changes in venous oxygenation in the renal vein during an oxygen challenge.

Manual definition of the kidneys to compute Total Kidney Volume (TKV) is a tedious and labour intensive bottleneck in many renal MRI studies. Here a Convolutional Neural Network (CNN) is developed to generate fully automated masks of the kidneys to compute TKV with better than human precision.

Finally, quantitative renal mapping methods are developed for an ex-vivo renal MRI protocol to enable future correlation with histopathology pipelines. Correlating these two diagnostic methods should aid clinical adoption of renal MRI, increase confidence in diagnostics, improved patient experience, and will have applications in nephrectomy studies and transplantation.

### About This Repository

If you're at the point you want to look at the LaTeX "code" someone else wrote for their thesis then you're probably in the process/about to start writing your own. You'll probably therefore understand that although you write the thesis at the end of your PhD, it's pulling from the previous three/four years of work, as such, there are some inconsistencies in this repo, things like vector image file formats, its just a product of the work being spread over such a long period of time and workflows changing. Basically don't see this as the "Alex approved thesis writing/typesetting method" and use your own judgement.

Probably the most useful bit of code here are the pulse sequence diagrams in the theory chapter. These were all programmed up in Python. Again, there's not a huge amount of consistency between scripts, in hindsight I should have made a little Python package for drawing the diagrams but didn't have time when I was writing. The code should still be useful and make a good starting point for anyone else to adapt into their own PSDs though. Most of them are located [here](https://github.com/alexdaniel654/Thesis/tree/master/Images/Theory).

<object data="https://github.com/alexdaniel654/Thesis/blob/master/Images/Theory/spin_warp/spin_warp.pdf" type="application/pdf" width="700px" height="700px">
    <embed src="https://github.com/alexdaniel654/Thesis/blob/master/Images/Theory/spin_warp/spin_warp.pdf">
        <p>This browser does not support PDFs. Please download the PDF to view it: <a href="https://github.com/alexdaniel654/Thesis/blob/master/Images/Theory/spin_warp/spin_warp.pdf">Download PDF</a>.</p>
    </embed>
</object>

If you have any questions about the thesis, figures or LaTeX feel free to [drop me an email](mailto:alexander.daniel@nottingham.ac.uk).