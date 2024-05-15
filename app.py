from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message 

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.office365.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'cisnerosprojects@outlook.com'
app.config['MAIL_PASSWORD'] = 'toetvyvyaujztkom'
mail = Mail(app)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    team_members = [
        {'name':'Sophia Chen', 'role':'Piano', 'bio':'Sophia Chen, a masterful classical pianist, has dedicated 18 years to piano performance and teaching. She is a recipient of the International Piano Award and holds an MMus from the Royal College of Music, London.', 'image_file':'images/about-us/Chen.JPG'},
        {'name':'Miles Robinson', 'role':'Voice', 'bio':'An African-American jazz vocalist and Grammy nominee, Robinson has 20 years of experience in jazz vocal and improvisation. He graduated from the New School for Jazz and Contemporary Music and is renowned for his soulful performances.', 'image_file':'images/about-us/Robinson.JPG'},
        {'name':'Ava Johnson', 'role':'Voice', 'bio':'Johnson has been a holistic vocal instructor for 12 years. She has an MA in Vocal Performance from MSM and has garnered nationwide recognitio for NYSSMA exams preparation.', 'image_file':'images/about-us/Johnson.JPG'},
        {'name':'Noah Kim', 'role':'Piano & Theory', 'bio':'Kim is both a pianist and music theory instructor with 15 years of experience. He authored a series of popular music theory textbooks and holds an MMus from the University of Toronto, Canada.', 'image_file':'images/about-us/Kim.JPG'},
        {'name':'Emily Clarke', 'role':'Saxophone', 'bio':'British saxophonist Clarke, with 30 years of experience, specializes in jazz and classical saxophone. She was the youngest winner of the National Saxophone Congress Competition and is a graduate of the New England Conservatory.', 'image_file':'images/about-us/Clarke.JPG'},
        {'name':'Jordan Fisher', 'role':'Piano & Composition', 'bio':'An American contemporary pianist, composer, and educator, Jordan Fisher has 14 years of experience. He is known for composing scores for award-winning indie films and holds an MFA from the California Institute of the Arts.', 'image_file':'images/about-us/Fisher.JPG'},
        {'name':'Maria Gonzales', 'role':'Voice & Theater', 'bio':'Cuban soprano,  Gonzales, is a graduate of Universidad de las Artes, Havana. She is a veteran in operatic and musical theater performance with 20 years of experience in Broadway and West End productions.', 'image_file':'images/about-us/Gonzales.JPG'},
        {'name':'Isabelle Dubois', 'role':'Guitar & Bass', 'bio':'French musician  Dubois, a classical guitarist and bass player, has 12 years of experience. She is a winner of the International Guitar Competition and studied at the Conservatoire de Paris.', 'image_file':'images/about-us/Dubois.JPG'},
        {'name':'Oliver Bennett', 'role':'Piano, Harp, & Theory', 'bio':'Belgian multi-instrumentalist and composer, Bennett, has over 50 years of experience. He has premiered compositions at international music festivals and holds an MA in Composition from the Royal Conservatory of Brussels.', 'image_file':'images/about-us/Bennett.JPG'},
        {'name':'Hye-Jin Park', 'role':'Piano & Violin', 'bio':'Park is a piano and violin instructor fluent in Korean and English. With 10 years of experience, she is an acclaimed performer in Asia and the US and studied at Seoul National University and the Manhattan School of Music.', 'image_file':'images/about-us/Park.JPG'},
        {'name':'Nadia Petrova', 'role':'Theory & Composition', 'bio':'Composer Petrova is renowned for her theory expertise, and pianism. With 13 years of experience, she holds a Doctorate in MC from the Moscow Conservatory.', 'image_file':'images/about-us/Petrova.JPG'},
        {'name':'Thomas Lee', 'role':'Violin & Orchestra', 'bio':'Lee is an orchestra violinist and instructor with 17 years of experience. An accomplished conductor, he has led orchestras in Europe and Asia and holds an MMus in Conducting from the Vienna University of Music and Performing Arts.', 'image_file':'images/about-us/Lee.JPG'}
    ]
    return render_template('about.html', team_members=team_members)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':

        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone = request.form['phone']
        subject = request.form['subject']
        message = request.form['message']

        msg = Message (subject, sender = 'cisnerosprojects@outlook.com', recipients = ['cisnerosprojects@outlook.com'])
        msg.body = f"From: {first_name} {last_name}\nEmail: {email}\nPhone: {phone}\n\n{message}"
        mail.send(msg)

        return render_template('contact.html', success=True) 
    return render_template('contact.html')

@app.route('/programs')
def programs():
    programs = [
        {'name':'Piano', 'description':'Our piano classes cater to students of all levels, from beginners discovering the keys for the first time to advanced musicians honing their concert repertoire. Instruction covers a range of techniques, theory, sight-reading, and performance practices, ensuring a comprehensive understanding of piano playing. Specialized courses are available, focusing on classical, jazz, and contemporary genres, tailored to align with your musical passion and goals.', 'image_file':'images/programs/piano.JPG'},
        {'name':'Strings', 'description':'The string program offers individualized instruction on a variety of instruments including violin, viola, cello, and double bass. Classes are designed to suit all proficiency levels, introducing beginners to the basics of string playing and offering advanced players in-depth studies in bowing techniques, vibrato, and repertoire expansion. Ensemble opportunities provide a platform for performance and collaboration among peers.', 'image_file':'images/programs/strings.JPG'},
        {'name':'Winds', 'description':'Wind instrument instruction encompasses a broad array of classes for flute, clarinet, saxophone, trumpet, and more. Each class is tailored to student level, from novices learning breath control and tone production to advanced students mastering complex solos and ensemble pieces. Special emphasis is placed on tone development, technical skills, and musicality across genres from classical to jazz.', 'image_file':'images/programs/winds.JPG'},
        {'name':'Guitar', 'description':'Our guitar program welcomes students interested in classical, acoustic, and electric guitar disciplines. Beginners start with the fundamentals of strumming and chord progression, while intermediate and advanced students explore various playing styles, improvisation, and composition. Specialty classes are available for those looking to delve into specific genres such as blues, rock, and fingerstyle guitar.', 'image_file':'images/programs/guitar.JPG'},
        {'name':'Voice', 'description':'Voice lessons are designed for singers at all stages of their journey, offering techniques in breath control, pitch accuracy, and vocal range expansion. Classes cover a variety of musical styles, from classical opera to modern pop, helping students develop a versatile and expressive vocal performance. Personalized coaching focuses on your unique voice, fostering confidence and stage presence.', 'image_file':'images/programs/voice.JPG'},
        {'name':'Music Theory', 'description':'Our music theory classes demystify the language of music, offering students of all instruments a foundation in reading music, understanding harmony, and exploring composition. From the basics of notation to the complexities of harmonic analysis, these classes enhance practical performance skills and deepen musical appreciation.', 'image_file':'images/programs/theory.JPG'},
        {'name':'Band & Orchestra', 'description':'The band and orchestra program provides an immersive group playing experience, catering to wind, brass, string, and percussion instrumentalists. Students engage in ensemble work, refining their collaborative skills while exploring a diverse repertoire. The program is structured to accommodate different skill levels, with groups for beginners, intermediate, and advanced musicians.', 'image_file':'images/programs/orchestra.JPG'},
        {'name':'Introduction to Music', 'description':'Designed for complete beginners of any age, our Introduction to Music classes lay the groundwork for a lifelong appreciation and understanding of music. Adults and children alike are introduced to the fundamentals of music theory, instrument exploration, and basic performance skills. Tailored classes ensure that young learners receive age-appropriate instruction while adults can enjoy a curriculum designed for their unique needs and pace of learning.', 'image_file':'images/programs/intro.JPG'}
    ]
    return render_template('programs.html', programs=programs)

@app.route('/gallery')
def gallery():
    albums = [
        {"name": "Musical Theater", 
         "cover_image": "images/gallery/theater/theater1.jpg", 
         "images": ["images/gallery/theater/theater1.jpg", "images/gallery/theater/theater2.jpg" , "images/gallery/theater/theater3.jpg", "images/gallery/theater/theater4.jpg", "images/gallery/theater/theater5.jpg" , "images/gallery/theater/theater6.jpg"]
        },
        {"name": "Chamber Choirs", 
         "cover_image": "images/gallery/chamber/chamber1.jpg", 
         "images": ["images/gallery/chamber/chamber1.jpg", "images/gallery/chamber/chamber2.jpg" , "images/gallery/chamber/chamber3.jpg", "images/gallery/chamber/chamber4.jpg", "images/gallery/chamber/chamber5.jpg" , "images/gallery/chamber/chamber6.jpg"]
        },
        {"name": "SCCM Through The Years", 
         "cover_image": "images/gallery/sccm/sccm1.jpg", 
         "images": ["images/gallery/sccm/sccm1.jpg", "images/gallery/sccm/sccm2.jpg" , "images/gallery/sccm/sccm3.jpg", "images/gallery/sccm/sccm4.jpg", "images/gallery/sccm/sccm5.jpg" , "images/gallery/sccm/sccm6.jpg"]
        }
    ]

    all_images = [image for album in albums for image in album['images']]
    return render_template('gallery.html', albums=albums, all_images=all_images)
   

if __name__ == '__main__':
    app.run(debug=True)