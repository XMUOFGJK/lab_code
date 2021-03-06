clear; close all;
%% settings
folder = 'Train/General-100';%
savepath = 'train.h5';%
size_input = 11;% There are 4 pixels padding. Paper presents 7 size of fsub+4
size_label = 19;% (11-4) *3 - (3-1) size for caffe deconv: n*fsub-n+1
scale = 3;
stride = 4;

%% initialization
data = zeros(size_input, size_input, 1, 1);
label = zeros(size_label, size_label, 1, 1);
padding = abs(size_input - size_label)/2;
count = 0;

%% generate data
filepaths = dir(fullfile(folder,'*.bmp'));

for i = 1 : length(filepaths)
    
    image = imread(fullfile(folder, filepaths(i).name));
    image = rgb2ycbcr(image);
    image = im2double(image(:, :, 1));
    
    im_label = modcrop(image, scale);
    % LR image
    im_input = imresize(im_label, 1/scale, 'bicubic');
    [hei,wid] = size(im_input);
    
    % crop every imput of size_input
    for x = 1 : stride : hei - size_input + 1
        for y = 1 : stride : wid - size_input + 1

            % get start point of corresponding HR image
            % how to locate?
            % each time move stride*scale pixels
            locx = scale * (x + floor((size_input - 1)/2)) - floor((size_label + scale)/2 - 1);
            locy = scale * (y + floor((size_input - 1)/2)) - floor((size_label + scale)/2 - 1);
            
            % input and lable subimages
            subim_input = im_input(x : size_input + x - 1, y : size_input + y - 1);
            subim_label = im_label(locx : size_label + locx - 1, locy : size_label + locy - 1);
            
            count = count + 1;
            data(:, :, 1, count) = subim_input;
            label(:, :, 1, count) = subim_label;
        end
    end
end
% random the order
order = randperm(count);
data = data(:, :, 1, order);
label = label(:, :, 1, order); 

%% writing to HDF5
chunksz = 128;
created_flag = false;
totalct = 0;

% batchno is batch number, every 128 images form a batch
for batchno = 1:floor(count/chunksz)
    last_read = (batchno-1)*chunksz;
    % form batch input and label images
    batchdata = data(:,:,1,last_read+1:last_read+chunksz); 
    batchlabs = label(:,:,1,last_read+1:last_read+chunksz);

    % point at which to start writing data
    startloc = struct('dat',[1,1,1,totalct+1], 'lab', [1,1,1,totalct+1]);
    curr_dat_sz = store2hdf5(savepath, batchdata, batchlabs, ~created_flag, startloc, chunksz); 
    created_flag = true;
    % point to last data
    totalct = curr_dat_sz(end);
end
h5disp(savepath);

