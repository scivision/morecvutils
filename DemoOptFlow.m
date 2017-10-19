function flows = test_optflow(I)
if verLessThan('matlab','R2015a')
    error('this Python Matlab Engine demo requires Matlab >= R2015a')
end
if nargin==0
    I = genuint8();
end

disp(['passing into Matlab array of type ',class(I), ' and shape ',num2str(size(I))])

of = opticalFlowHS;

flows = nan(size(I),'single');

for i = 1:size(I,1)
    
    F = estimateFlow(of, squeeze(I(i,:,:)));
    flows(i,:,:) = F.Magnitude;

end

end

function I = genuint8()
    I = uint8(rand(10,512,512)*255);
end
