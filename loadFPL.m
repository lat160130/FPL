function [val] = loadFPL(fname)
% loads premier league json data into the matlab explorer
fid = fopen(fname); 
raw = fread(fid,inf); 
str = char(raw'); 
fclose(fid); 
val = jsondecode(str);

end

