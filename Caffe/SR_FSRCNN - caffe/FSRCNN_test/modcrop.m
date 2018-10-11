function imgs = modcrop(imgs, modulo)
if size(imgs,3)==1
<<<<<<< HEAD
=======
    % crop image with one channel
>>>>>>> Update
    sz = size(imgs);
    sz = sz - mod(sz, modulo);
    imgs = imgs(1:sz(1), 1:sz(2));
else
<<<<<<< HEAD
=======
    % crop image with more than one channel
>>>>>>> Update
    tmpsz = size(imgs);
    sz = tmpsz(1:2);
    sz = sz - mod(sz, modulo);
    imgs = imgs(1:sz(1), 1:sz(2),:);
end

