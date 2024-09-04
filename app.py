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
        {
            'name':'Sophia Chen', 
            'role':'Piano', 
            'bio':'Sophia Chen, a masterful classical pianist, has dedicated 18 years to piano performance and teaching. She is a recipient of the International Piano Award and holds an MMus from the Royal College of Music, London.', 
            'image_file':'images/about-us/Chen.JPG', 
            'image_description': "Portrait of Sophia Chen, a masterful classical pianist, posing with her hand partially covering her face against a rich red background, her expression introspective and poised.",
        },
        {
            'name':'Miles Robinson', 
            'role':'Voice', 
            'bio':'An African-American jazz vocalist and Grammy nominee, Robinson has 20 years of experience in jazz vocal and improvisation. He graduated from the New School for Jazz and Contemporary Music and is renowned for his soulful performances.', 
            'image_file':'images/about-us/Robinson.JPG',
            'image_description':"Close-up portrait of Miles Robinson, a jazz vocalist and Grammy nominee, looking directly into the camera with a serious expression, wearing a white shirt against a light background.",
        },
        {
            'name':'Ava Johnson', 
            'role':'Voice', 
            'bio':'Johnson has been a holistic vocal instructor for 12 years. She has an MA in Vocal Performance from MSM and has garnered nationwide recognitio for NYSSMA exams preparation.', 
            'image_file':'images/about-us/Johnson.JPG',
            'image_description':"Portrait of Ava Johnson, a voice instructor with braided hair, smiling warmly in a cream-colored top, set against a soft green background.",
        },
        {
            'name':'Noah Kim', 
            'role':'Piano & Theory', 
            'bio':'Kim is both a pianist and music theory instructor with 15 years of experience. He authored a series of popular music theory textbooks and holds an MMus from the University of Toronto, Canada.', 
            'image_file':'images/about-us/Kim.JPG',
            'image_description':"Portrait of Noah Kim, a middle-aged music theory and piano instructor, smiling gently with a light beard and mustache, dressed in a casual light blue shirt under a beige blazer, against a plain light background.",
        },
        {
            'name':'Emily Clarke', 
            'role':'Saxophone', 
            'bio':'British saxophonist Clarke, with 30 years of experience, specializes in jazz and classical saxophone. She was the youngest winner of the National Saxophone Congress Competition and is a graduate of the New England Conservatory.', 
            'image_file':'images/about-us/Clarke.JPG',
            'image_description':"Portrait of Emily Clarke, a seasoned saxophonist, smiling warmly at the camera. She has shoulder-length gray hair and is wearing a white turtleneck sweater with a beige cardigan draped over her shoulders, against a neutral background.",
        },
        {
            'name':'Jordan Fisher', 
            'role':'Piano & Composition', 
            'bio':'An American contemporary pianist, composer, and educator, Jordan Fisher has 14 years of experience. He is known for composing scores for award-winning indie films and holds an MFA from the California Institute of the Arts.', 
            'image_file':'images/about-us/Fisher.JPG',
            'image_description':"Portrait of Jordan Fisher, an American pianist and composer, looking thoughtfully at the camera with his chin resting on his hand. He has short blonde hair and is wearing a black shirt. His expression is serious, highlighting his focused personality.",
        },
        {
            'name':'Maria Gonzales', 
            'role':'Voice & Theater', 
            'bio':'Cuban soprano,  Gonzales, is a graduate of Universidad de las Artes, Havana. She is a veteran in operatic and musical theater performance with 20 years of experience in Broadway and West End productions.', 
            'image_file':'images/about-us/Gonzales.JPG',
            'image_description':"Portrait of Maria Gonzales, a Cuban soprano with a vibrant smile, captured indoors. She is wearing a chunky gold necklace and a cozy white sweater. Her short black hair frames her cheerful face, which radiates warmth and approachability.",
        },
        {
            'name':'Isabelle Dubois', 
            'role':'Guitar & Bass', 
            'bio':'French musician  Dubois, a classical guitarist and bass player, has 12 years of experience. She is a winner of the International Guitar Competition and studied at the Conservatoire de Paris.', 
            'image_file':'images/about-us/Dubois.JPG',
            'image_description':"Portrait of Isabelle Dubois, a youthful French musician with a charming smile, set against an autumnal background. She has light brown hair, freckles, and a subtle makeup look, complemented by a casual grey top under a beige coat.",
        },
        {
            'name':'Oliver Bennett', 
            'role':'Piano, Harp, & Theory', 
            'bio':'Belgian multi-instrumentalist and composer, Bennett, has over 50 years of experience. He has premiered compositions at international music festivals and holds an MA in Composition from the Royal Conservatory of Brussels.', 
            'image_file':'images/about-us/Bennett.JPG',
            'image_description':"Portrait of Oliver Bennett, an elderly Belgian musician with a distinguished long white beard and glasses. He has a thoughtful expression, gazing intently at the camera, dressed in a black shirt, set against a dark background.",
        },
        {
            'name':'Hye-Jin Park', 
            'role':'Piano & Violin', 
            'bio':'Park is a piano and violin instructor fluent in Korean and English. With 10 years of experience, she is an acclaimed performer in Asia and the US and studied at Seoul National University and the Manhattan School of Music.', 
            'image_file':'images/about-us/Park.JPG',
            'image_description':"Portrait of Hye-Jin Park, a young Asian musician with stylish bleached blonde hair and round glasses. She is wearing a black sweater over a white collared shirt, exuding a calm and collected demeanor. The background is softly blurred, emphasizing her focused expression.",
        },
        {
            'name':'Nadia Petrova', 
            'role':'Theory & Composition', 
            'bio':'Composer Petrova is renowned for her theory expertise, and pianism. With 13 years of experience, she holds a Doctorate in MC from the Moscow Conservatory.', 
            'image_file':'images/about-us/Petrova.JPG',
            'image_description':"Portrait of Nadia Petrova, a Caucasian woman with a thoughtful expression. She features a distinctive bob haircut with bangs and has freckles across her face. Wearing a black leather jacket over a white t-shirt, she poses against a rustic brick wall background, looking directly at the camera with a subtle confidence.",
         },
        {
            'name':'Thomas Lee', 
            'role':'Violin & Orchestra', 
            'bio':'Lee is an orchestra violinist and instructor with 17 years of experience. An accomplished conductor, he has led orchestras in Europe and Asia and holds an MMus in Conducting from the Vienna University of Music and Performing Arts.', 
            'image_file':'images/about-us/Lee.JPG',
            'image_description':"Portrait of Thomas Lee, an Asian man with a warm smile, seated against a wooden backdrop. He has short, slightly tousled black hair and is dressed in a casual white t-shirt. His friendly demeanor and youthful appearance reflect his approachable nature.",
        }
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
        {
            'name':
            'Piano', 
            'description':'Our piano classes cater to students of all levels, from beginners discovering the keys for the first time to advanced musicians honing their concert repertoire. Instruction covers a range of techniques, theory, sight-reading, and performance practices, ensuring a comprehensive understanding of piano playing. Specialized courses are available, focusing on classical, jazz, and contemporary genres, tailored to align with your musical passion and goals.', 
            'image_file':'images/programs/piano.JPG',
            'image_description':"A young girl with long brown hair tied back with clips, wearing a pink floral dress, concentrates as she plays the piano in a well-lit room.",
        },
        {
            'name':
            'Strings', 
            'description':'The string program offers individualized instruction on a variety of instruments including violin, viola, cello, and double bass. Classes are designed to suit all proficiency levels, introducing beginners to the basics of string playing and offering advanced players in-depth studies in bowing techniques, vibrato, and repertoire expansion. Ensemble opportunities provide a platform for performance and collaboration among peers.', 
            'image_file':'images/programs/strings.JPG',
            'image_description':"A woman in a red sweater assists a young girl in a yellow sweatshirt with holding a violin correctly, both focused intently on the music stand in front of them.",
        },
        {
            'name':'Winds',
            'description':'Wind instrument instruction encompasses a broad array of classes for flute, clarinet, saxophone, trumpet, and more. Each class is tailored to student level, from novices learning breath control and tone production to advanced students mastering complex solos and ensemble pieces. Special emphasis is placed on tone development, technical skills, and musicality across genres from classical to jazz.',
            'image_file':'images/programs/winds.JPG',
            'image_description':"A young boy with curly red hair, dressed in a green sweater, plays the flute while a teenage girl stands nearby holding a flute, both in front of a music stand in a well-lit room.",
        },
        {
            'name':'Guitar',
            'description':'Our guitar program welcomes students interested in classical, acoustic, and electric guitar disciplines. Beginners start with the fundamentals of strumming and chord progression, while intermediate and advanced students explore various playing styles, improvisation, and composition. Specialty classes are available for those looking to delve into specific genres such as blues, rock, and fingerstyle guitar.',
            'image_file':'images/programs/guitar.JPG',
            'image_description':"A young boy with short hair sits and plays an acoustic guitar, focused on sheet music placed on a stand in front of him against a textured wall.",
        },
        {
            'name':'Voice',
            'description':'Voice lessons are designed for singers at all stages of their journey, offering techniques in breath control, pitch accuracy, and vocal range expansion. Classes cover a variety of musical styles, from classical opera to modern pop, helping students develop a versatile and expressive vocal performance. Personalized coaching focuses on your unique voice, fostering confidence and stage presence.',
            'image_file':'images/programs/voice.JPG',
            'image_description':"A young girl with a high ponytail smiles brightly while holding a microphone. She stands in front of a music stand with sheet music, against a background of acoustic foam panels.",
        },
        {
            'name':'Music Theory',
            'description':'Our music theory classes demystify the language of music, offering students of all instruments a foundation in reading music, understanding harmony, and exploring composition. From the basics of notation to the complexities of harmonic analysis, these classes enhance practical performance skills and deepen musical appreciation.',
            'image_file':'images/programs/theory.JPG',
            'image_description':"A hand with a ring writes musical notes and symbols, including a treble clef and sharps, on a blackboard using white chalk.",
        },
        {
            'name':'Band & Orchestra',
            'description':'The band and orchestra program provides an immersive group playing experience, catering to wind, brass, string, and percussion instrumentalists. Students engage in ensemble work, refining their collaborative skills while exploring a diverse repertoire. The program is structured to accommodate different skill levels, with groups for beginners, intermediate, and advanced musicians.',
            'image_file':'images/programs/orchestra.JPG',
            'image_description':"Two young musicians, a man and a woman, play cellos in an orchestra, both focused intently on their performance on stage.",
        },
        {
            'name':'Introduction to Music',
            'description':'Designed for complete beginners of any age, our Introduction to Music classes lay the groundwork for a lifelong appreciation and understanding of music. Adults and children alike are introduced to the fundamentals of music theory, instrument exploration, and basic performance skills. Tailored classes ensure that young learners receive age-appropriate instruction while adults can enjoy a curriculum designed for their unique needs and pace of learning.',
            'image_file':'images/programs/intro.JPG',
            'image_description':"A group of young children, seated in a circle in a colorful classroom, playing with hand bells as part of a music lesson. A teacher is guiding them through the activity.",
        }
    ]
    return render_template('programs.html', programs=programs)

@app.route('/gallery')
def gallery():
    albums = [
        {"name": "Musical Theater", 
         "cover_image": "images/gallery/theater/theater1.jpg", 
         "cover_alt": "Cover image of the Musical Theater album showing a dramatic stage scene with two young children.",
         "images": [
             {"url": "images/gallery/theater/theater1.jpg", "alt": "Two children perform on stage during a musical theater festival at SCCM, surrounded by stage decorations and red curtains."},
             {"url": "images/gallery/theater/theater2.jpg", "alt": "A group of theater students and a director engaged in a discussion during a rehearsal on stage, illuminated by bright stage lights."},
             {"url": "images/gallery/theater/theater3.jpg", "alt": "Three actors in period costumes, including a woman in a white gown and two men in formal suits and top hats, perform a scene with candlelight in the background."},
             {"url": "images/gallery/theater/theater4.jpg", "alt": "A large ensemble of performers in historical costumes sing and gesture dramatically during a musical theater performance."},
             {"url": "images/gallery/theater/theater5.jpg", "alt": "Three actors in medieval-style costumes, sitting and standing around a table with lit candles, performing a dramatic scene."},
             {"url": "images/gallery/theater/theater6.jpg", "alt": "A group of performers in extravagant wigs and costumes engage in a lively dance on a brightly lit stage, with a colorful backdrop depicting a carnival scene."}
         ]
        },
        {"name": "Chamber Choirs", 
         "cover_image": "images/gallery/chamber/chamber1.jpg", 
         "cover_alt": "Cover image of the Chamber Choirs album showing choir members mid-song during a performance.",
         "images": [
             {"url": "images/gallery/chamber/chamber1.jpg", "alt": "Male choir in matching gray vests and black bow ties sing passionately in a choir performance."},
             {"url": "images/gallery/chamber/chamber2.jpg", "alt": "A male choir with members dressed in gray vests and black bow ties performing on stage with focused expressions."},
             {"url": "images/gallery/chamber/chamber3.jpg", "alt": "Student choir holding yellow flowers while singing, led by a conductor in a white shirt, during a rehearsal."},
             {"url": "images/gallery/chamber/chamber4.jpg", "alt": "Boys choir, each holding a yellow flower, attentively following the conductor's lead in a church setting."},
             {"url": "images/gallery/chamber/chamber5.jpg", "alt": "Choir conductor leading a group of students holding lit candles during a solemn performance in a church."},
             {"url": "images/gallery/chamber/chamber6.jpg", "alt":  "Mixed adult chamber choir, dressed in black, singing from sheet music during a practice session."}
         ]
        },
        {"name": "SCCM Family Through The Years", 
         "cover_image": "images/gallery/sccm/sccm1.jpg", 
         "cover_alt": "Cover image of the SCCM Through The Years Album showing a music teacher instructing children around a table with music sheets and recorders.",
         "images": [
             {"url": "images/gallery/sccm/sccm1.jpg", "alt": "A music teacher wearing a pink mask instructs a diverse group of children, all wearing masks, around a table filled with music sheets and recorders, highlighting a moment in the SCCM's history of adapting music education during a pandemic."},
             {"url": "images/gallery/sccm/sccm2.jpg", "alt": "A young girl concentrating while playing a harp, with sheet music visible on the right."},
             {"url": "images/gallery/sccm/sccm3.jpg", "alt": "Three musicians performing a classical guitar piece on stage, with a grand piano in the background."},
             {"url": "images/gallery/sccm/sccm4.jpg", "alt": "A music teacher claps along with two young students, one singing and the other playing a small guitar, during a lesson at SCCM."},
             {"url": "images/gallery/sccm/sccm5.jpg", "alt": "A young student at SCCM holds a microphone and reads sheet music with a teacher, standing next to an open piano."},
             {"url": "images/gallery/sccm/sccm6.jpg", "alt": "A music teacher at SCCM sits at a piano with a group of young students, engaging them in a lesson."}
         ]
        }
    ]

    all_images = [image['url'] for album in albums for image in album['images']]
    return render_template('gallery.html', albums=albums, all_images=all_images)
   

if __name__ == '__main__':
    app.run(debug=True)