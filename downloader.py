import os;
fob = open ( 'files.txt', "r" );
lines = fob.readlines();
fob.close();
lines = [e.replace('\n', '') for e in lines];
exe_name='youtube-dl'
cmd_line_opt = '\
-i \
--yes-playlist \
--restrict-filenames \
--write-sub \
--sub-format srt \
--sub-lang en'
youtube_dl_path='.\\'
cmd_line_srt=youtube_dl_path + exe_name + ' ' + cmd_line_opt + ' %s'
fob1 = open ( "files.bak", "w" );
fob1.write ( "\n".join( lines ) );
fob1.close();
lines1 = lines;
for f in lines:
    cmd_line = cmd_line_srt % (f)
    print ( cmd_line );
    os.system ( cmd_line );
    lines1.remove ( f );
    fob1 = open ( "files.txt", "w" );
    fob1.write ( "\n".join ( lines1 ) );
    fob1.close();
    
