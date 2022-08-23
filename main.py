import datetime
import time

def make_entry_str(content, epoch, title):
    template = '''
    "photos" : [],
    "timezone" : "America\/Toronto",
    "label" : "",
    "type" : "markdown",
    "music_title" : "",
    "tags" : [],
    "lat" : 1.7976931348623157e+308,
    "sentiment" : 0,
    "date_modified" : {epoch},
    "preview_text" : "",
    "mood" : 0,
    "favourite" : false,
    "text" : "{title} \\n{content}",
    "id" : "{epoch}-3fd440eae0942322",
    "music_artist" : "",
    "date_journal" : {epoch},
    "folder" : "",
    "address" : "",
    "lon" : 1.7976931348623157e+308,
    '''.format(content=content, epoch=epoch, title=title)

    weather =   '''
    "weather" : {
    "id" : 0,
    "place" : "",
    "description" : "",
    "icon" : "",
    "degree_c" : 1.7976931348623157e+308
    }''' 
    
    return '{' + template + weather + '}' 

# Open text file
with open('entries.txt') as file:

    # Read text file
    text = file.read()
    entries = text.split('______________________________________________________________________________')
    
    for entry in entries:
        date = ''
        title = ''
        content = ''
        counter = 0
        
        for line in entry.split('\n'):
            if line != '':
                if counter == 0:
                    date = line 
                    counter += 1
                elif counter == 1:
                    title = line
                    counter += 1
                else:
                    content = line
                    counter += 1

            # All data gathered for entry
            # Create entry and reset counter
            if counter == 3:

                counter = 0

                # Get epoch from date
                timestruct = time.strptime(date, "%H:%M %p, %d %B %Y")
                epoch = int(time.mktime(timestruct)) * 1000 

                # Create entry
                json = make_entry_str(content, epoch, title)  

                file_name = str(epoch) + '.json'
                new_file = open(file_name, "w")
                new_file.write(json)

                

            

