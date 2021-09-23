from django.db.models import Q

from .models import Project, Review, Tag

SEP = 9
# working with qs of one2Many and ManyToMany

# ################## #################  # #################  # #################  # #################
# all projects
projects = Project.objects.all()

print(projects)

print("#" * 100)

# ################## #################  # #################  # #################  # #################
# get sehhaty app

sehhaty = Project.objects.get(title__iexact="sehhaty")

# ################## #################  # #################  # #################  # #################

# get reviews of sehhaty
sehhaty_reviews = sehhaty.reviews.all()

print(sehhaty)

print("#" * 100)

print(sehhaty_reviews)

# ################## #################  # #################  # #################  # #################


# get all projects that contain 'very' in the review body

# attr__attr__expression ==> obj__att__expression
projects = Project.objects.filter(reviews__body__icontains="very")

print(projects)

projects = Project.objects.filter(reviews__body__icontains="app").distinct()

# ################## #################  # #################  # #################  # #################

# get 'Projects' that use django 'Tag'

django = Tag.objects.get(name__iexact="django")
projects_of_django = django.projects.all()  # ===> tagObj.related_name.all()
projects_of_django_2 = (
    django.projects_list()
)  # ===> tagObj.custom_method() ==> return related projects

print("#" * 50)
print(django)

print(projects_of_django)

# ################## #################  # #################  # #################  # #################

# get tools used in one project

ecoommerce = Project.objects.get(title__iexact="ecoommerce")
print("#" * 50)
print(ecoommerce)

tags_of_ecoommerce = ecoommerce.tags.all()
print(tags_of_ecoommerce)
tags_of_ecoommerce = ecoommerce.tags_list()
print(tags_of_ecoommerce)

# ################## #################  # #################  # #################  # #################


# add/remove using m2m relationship ===> from Project side

# add 'Tag' flask from 'Project'  blog

print("*" * 100)
flask = Tag.objects.get(name__iexact="flask")
blog = Project.objects.get(title__iexact="blog")

print(blog.tags.all())
blog.tags.add(flask)
print(blog.tags.all())

# ################## #################  # #################  # #################  # #################

# remove 'Tag' django from 'Project'  blog
blog.tags.remove(django)
print(blog.tags.all())

# ################## #################  # #################  # #################  # #################

# add/remove using m2m relationship ===> from Tag side

# create new 'Tag' and add it to 'Projects' youtube & instgram
aws = Tag.objects.create(name="AWS")
youtube = Project.objects.get(title__iexact="youtube")
instgram = Project.objects.get(title__iexact="instgram")
facebook = Project.objects.get(title__iexact="facebook")

aws.projects.add(youtube)
aws.projects.add(instgram)

# ################## #################  # #################  # #################  # #################

# add/remove using one2m relationship

call_center_review = Review.objects.create(
    body="Fast Call center support", proj=instgram
)

youtube.reviews.add(call_center_review)


great_service = Review.objects.create(body="NICE SERVICE", proj=blog)

ecoommerce.reviews.add(great_service)

great = Review.objects.create(body="GREAT", proj=instgram)

facebook.reviews.add(great)

# # ################## #################  # #################  # #################  # #################
# set multiple tags to project
# from project side
docker = Tag.objects.create(name="Docker")
ansible = Tag.objects.create(name="Ansible")
google = Tag.objects.create(name="Google Cloud")
kubernetes = Tag.objects.create(name="Kubernetes")
ios = Tag.objects.create(name="IOS")
android = Tag.objects.create(name="Android")
flutter = Tag.objects.create(name="Flutter")

blog.tags.set([docker, ansible, google])  # replace and set new list

blog.tags.add(kubernetes, aws, django)  # add new tags to project blog

# # ################## #################  # #################  # #################  # #################
# set multiple tags to project
# from tag side
anat = Project.objects.get(title__iexact="anat")
gcc = Project.objects.get(title__iexact="gcc")

ios.projects.set([anat, gcc])
android.projects.add(gcc)

flutter.projects.set([youtube])
# from apps.projects import shell

vscode = Tag.objects.create(name="Vscode")
pycharm = Tag.objects.create(name="Pycharm")

youtube.tags.set([vscode, pycharm])

# # ################## #################  # #################  # #################  # #################
# exclude
not_social = Project.objects.exclude(
    Q(title__iexact="youtube")
    | Q(title__iexact="facebook")
    | Q(title__iexact="instgram")
)

print(not_social)

# # ################## #################  # #################  # #################  # #################

# filter by month
projects_in_sep = Project.objects.filter(created__month=SEP)


print(projects_in_sep)

# # ################## #################  # #################  # #################  # #################
# gt lt, lte

good_votes = Project.objects.filter(votes__gte=50)
bad_votes = Project.objects.filter(votes__lte=50)
vote_range = Project.objects.filter(votes__range=[35, 40])

print(good_votes)
print(bad_votes)

print("#" * 100)
print(vote_range)

# # ################## #################  # #################  # #################  # #################
# delete
grt = Review.objects.get(body__icontains="very cool app")
grt.delete()
