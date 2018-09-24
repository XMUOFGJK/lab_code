***********************************************************************************************************


Training code for "Accelerating the Super-Resolution Convolutional Neural Networks" (ECCV 2016) 
by Chao Dong (dongchao@sensetime.com)



***********************************************************************************************************



Usage:


1. Place the "FSRCNN" folder into "($Caffe_Dir)/examples/"



2. Open MATLAB and direct to ($Caffe_Dir)/example/FSRCNN, run 
"generate_train.m" and "generate_test.m" to generate training and test data.
You can also run data_aug.m to do data augmentation first.


3. To train our FSRCNN, run
./build/tools/caffe train --solver examples/FSRCNN/FSRCNN_solver.prototxt (For FSRCNN)
or
./build/tools/caffe train --solver examples/FSRCNN/FSRCNN-s_solver.prototxt (For FSRCNN-s)



4. After training, you can extract parameters from the caffe model and save them in the format that can be used in our test package (FSRCNN_test). To do this, you need to install mat-caffe first, then open MATLAB and direct to ($Caffe_Dir) and run "saveFilters.m". The "($Caffe_Dir)/examples/FSRCNN/FSRCNN.mat" will be there for you.


