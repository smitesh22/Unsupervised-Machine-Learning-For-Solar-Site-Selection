import torch.nn as nn

class AutoEncoder(nn.Module):
    def __init__(self):
        
        super().__init__()
        
        self.encoder = nn.Sequential( # input : 3601*3601
            nn.Conv2d(1, 32, kernel_size=(15, 15), stride=4, padding=1),
            nn.ReLU(),
            nn.Conv2d(32, 64, kernel_size=(8, 8), stride=4, padding=1),
            nn.ReLU(),
            nn.Conv2d(64, 128, kernel_size=(4, 4), stride=2, padding=1),
            nn.ReLU(),
            nn.Conv2d(128, 256, kernel_size=(4, 4), stride=2, padding=1),
            nn.ReLU(),
            nn.Conv2d(256, 512, kernel_size=(4, 4), stride=2, padding=1),
            nn.ReLU(),
            
        )
        
        self.decoder = nn.Sequential(
            nn.ConvTranspose2d(512, 256, kernel_size=(4, 4), stride=2, padding=1, output_padding=0),
            nn.ReLU(),
            nn.ConvTranspose2d(256, 128, kernel_size=(4, 4), stride=2, padding=1, output_padding=0),
            nn.ReLU(),
            nn.ConvTranspose2d(128, 64, kernel_size=(4, 4), stride=2, padding=1, output_padding=0),
            nn.ReLU(),
            nn.ConvTranspose2d(64, 32, kernel_size=(8, 8), stride=4, padding=1, output_padding=0),
            nn.ReLU(),
            nn.ConvTranspose2d(32, 1, kernel_size=(15, 15), stride=4, padding=1, output_padding=0),
            nn.Sigmoid(),  # Output is between 0 and 1
        )
        
    def forward(self, x):
        x = self.encoder(x)
        x = self.decoder(x)
        return x
            
    def dimensions(self, x):
        print(f"----------ENCODER----------")
        print(f"Input shape : {x.shape[1], x.shape[2], x.shape[3]}")
        x = self.encoder[0](x)
        print(f"After 1st Conv2d: {x.shape[1], x.shape[2], x.shape[3]}")
        x = self.encoder[1](x)
        print(f"After 1st ReLU: {x.shape[1], x.shape[2], x.shape[3]}")
        x = self.encoder[2](x)
        print(f"After 2nd Conv2d: {x.shape[1], x.shape[2], x.shape[3]}")
        x = self.encoder[3](x)
        print(f"After 2nd ReLU: {x.shape[1], x.shape[2], x.shape[3]}")
        x = self.encoder[4](x)
        print(f"After 3rd Conv2d: {x.shape[1], x.shape[2], x.shape[3]}")
        x = self.encoder[5](x)
        print(f"After 3rd ReLU: {x.shape[1], x.shape[2], x.shape[3]}")
        x = self.encoder[5](x)
        print(f"After 4th Conv2d: {x.shape[1], x.shape[2], x.shape[3]}")
        x = self.encoder[6](x)
        print(f"After 4th ReLU: {x.shape[1], x.shape[2], x.shape[3]}")
        x = self.encoder[7](x)
        print(f"After 5th Conv2d: {x.shape[1], x.shape[2], x.shape[3]}")
        x = self.encoder[8](x)
        print(f"After 6th ReLU: {x.shape[1], x.shape[2], x.shape[3]}")
        
        print("---------DECODER------------")
        x= self.decoder[0](x)
        print(f"After 1st Transpose: {x.shape[1], x.shape[2], x.shape[3]}")
        x = self.decoder[1](x)
        print(f"After 1st ReLU: {x.shape[1], x.shape[2], x.shape[3]}")
        x = self.decoder[2](x)
        print(f"After 2nd Transpose: {x.shape[1], x.shape[2], x.shape[3]}")
        x = self.decoder[3](x)
        print(f"After 2nd ReLU: {x.shape[1], x.shape[2], x.shape[3]}")
        x = self.decoder[4](x)
        print(f"After 3rd Transpose: {x.shape[1], x.shape[2], x.shape[3]}")
        x = self.decoder[5](x)
        print(f"After 3rd ReLU: {x.shape[1], x.shape[2], x.shape[3]}")
        x = self.decoder[6](x)
        print(f"After 4th Transpose: {x.shape[1], x.shape[2], x.shape[3]}")
        x = self.decoder[7](x)
        print(f"After 5th ReLU: {x.shape[1], x.shape[2], x.shape[3]}")
        x = self.decoder[8](x)
        print(f"Decoder output : {x.shape[1], x.shape[2], x.shape[3]}")