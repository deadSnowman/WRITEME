## SeetaFace Engine

### Description

**SeetaFace Engine** is an open source C++ face recognition engine, which can run on CPU with no third-party dependence. It contains three key parts, i.e., **SeetaFace Detection** , **SeetaFace Alignment** and **SeetaFace Identification** , which are necessary and sufficient for building a real-world face recognition applicaiton system. 

  * SeetaFace Detection implements a funnel-structured (FuSt) cascade schema for real-time multi-view face detection, which achieves a good trade-off between detection accuracy and speed. State of the art accuracy can be achieved on the public dataset @abstr_hyperlink in high speed. See @abstr_hyperlink for more details. 

  * SeetaFace Alignment cascades several stacked auto-encoder networks to detect landmarks in real time (more than @abstr_number fps on a single I @abstr_number desktop CPU), and achieves the state-of-the-art accuracy at least on some public datasets @abstr_hyperlink . See @abstr_hyperlink for more details. 

  * SeetaFace Identification is a modification of AlexNet CNN for face recognition, with better performance in terms of both accuracy ( @abstr_number . @abstr_number % on [LFW] (http://vis-www.cs.umass.edu/lfw/) and speed (about @abstr_number ms on a single I @abstr_number desktop CPU). See @abstr_hyperlink for more details. 




This face recognition engine is developed by Visual Information Processing and Learning (VIPL) group, Institute of Computing Technology, Chinese Academy of Sciences. The codes are written in C++ without dependence on any @abstr_number rd-party libraries. The open source is now released under BSD- @abstr_number license (see LICENSE for details), which means the codes can be used freely for both acedemic purpose and industrial products.

If you meet problems when using SeetaFace Engine, you may seek help from Configuration Documentation.

### Contact Info

If you have any problem on SeetaFace Engine, please contact us by sending email to SeetaFace@vipl.ict.ac.cn. If Seetaface can not meet your business needs, please contact business@seetatech.com for business cooperation. For more AI services, please visit SeetaTech official website: http://www.seetatech.com.

SeetaTech is a start-up company with the focus on computer vision technology, whose founding team comes from Visual Information Processing and Learning (VIPL) group, Institute of Computing Technology, Chinese Academy of Sciences. We have always been adhering to the development principle of "open source striving to develop AI", promoting the rapid integration of Artificial Intelligence and other industries.

### Other Documentation

  * SeetaFace Detection
  * SeetaFace Alignment
  * SeetaFace Identification

