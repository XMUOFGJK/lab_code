import torch
import torch.nn as nn

# Build the SRCNN model
class SRCNN(nn.Module):
    def __init__(self,IN_channel=3, N_gpu=1):# Use GPU
        super(SRCNN, self).__init__()
        self.ngpu = N_gpu
        # In SRCNN, totally three conv layers and two ReLU layers.
        self.main = torch.nn.Sequential(
            nn.Conv2d(in_channels=IN_channel,out_channels=64,kernel_size=9,stride=1,bias=True),
            nn.ReLU(inplace=True),
            nn.Conv2d(in_channels=64, out_channels=32, kernel_size=1, stride=1, bias=True),
            nn.ReLU(inplace=True),
            nn.Conv2d(in_channels=32, out_channels=3, kernel_size=5, stride=1, bias=True),
        )


    def forward(self,input):
        gpu_ids = None
        if isinstance(input.data, torch.cuda.FloatTensor) and self.ngpu > 1:
            gpu_ids = range(self.ngpu)
<<<<<<< HEAD
=======
        # multi GPU training: model, GPUid
>>>>>>> Update
        output = nn.parallel.data_parallel(self.main, input, gpu_ids)
        return output

