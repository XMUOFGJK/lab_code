import argparse
import torch
import torch.nn as nn
from network import SRCNN
import data_utils
from data_utils import TrainDatasetFromFolder
from torch.utils.data import DataLoader
import torch.optim as optim
from torch.autograd import Variable

# This method is for bicubic downsample only. If use nearest method to downsample image, it won't work.

# parser, used to compliment the help document
parser = argparse.ArgumentParser()

parser.add_argument('--HRdir', default='HRDataSet', help='HR dataset')
parser.add_argument('--LRdir',type=str, default='LRDataSet')
parser.add_argument('--ngpu', type=int, default=2, help='number of ngpu using')
parser.add_argument('--batchSize', type=int, default=8, help='input batch size')
parser.add_argument('--lr', type=float, default=2e-3, help='Learning rate')
parser.add_argument('--nepho', type=int, default=200, help='number of ngpu using')

# put parser's arguments in the args
args = parser.parse_args()

# generate LRImages
data_utils.generate_LRImage(args.HRdir,args.LRdir,3)

train_set = TrainDatasetFromFolder(args.HRdir,args.LRdir,upscale_factor=3)
train_loader = DataLoader(dataset=train_set, num_workers=4, batch_size=args.batchSize, shuffle=True)

model = SRCNN(3,N_gpu=args.ngpu)
criterion =  nn.MSELoss()

# Check if cuda could be used
if torch.cuda.is_available():
    model.cuda()
    criterion.cuda()

optimizer = optim.SGD(model.parameters(), lr = args.lr)

for e in range(args.nepho):
    for i,(data, target) in enumerate(train_loader):
        if torch.cuda.is_available():
            data, target = Variable(data).cuda(), Variable(target).cuda()
            predict = model(data)
            loss = criterion(predict,target)
            loss.backward()
            optimizer.step()

            loss_v = loss.data[0]
            print(loss_v)

if __name__ == '__main__':
   freeze_support()