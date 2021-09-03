from .models import Project, Tag, Review

# working with qs of one2Many and ManyToMany

# all projects
projects = Project.objects.all()

print(projects)

print("#" * 100)

# get sehhaty app
sehhaty = Project.objects.get(title__iexact="sehhaty")

# get reviews of sehhaty
sehhaty_reviews = sehhaty.reviews.all()

print(sehhaty)

print("#" * 100)

print(sehhaty_reviews)

# get all projects that contain 'very' in the review body

# attr__attr__expression ==> obj__att__expression
projects = Project.objects.filter(reviews__body__icontains="very")

print(projects)

projects = Project.objects.filter(reviews__body__icontains="app").distinct()

# get 'Projects' that use django 'Tag'

django = Tag.objects.get(name__iexact="django")
projects_of_django = django.projects.all()  # ===> tagObj.related_name.all()
projects_of_django_2 = django.projects_list()  # ===> tagObj.custom_method() ==> return related projects

print("#" * 50)
print(django)

print(projects_of_django)

# get tools used in one project

ecoommerce = Project.objects.get(title__iexact="ecoommerce")
print("#" * 50)
print(ecoommerce)

tags_of_ecoommerce = ecoommerce.tags.all()
print(tags_of_ecoommerce)
tags_of_ecoommerce = ecoommerce.tags_list()
print(tags_of_ecoommerce)

# from apps.projects import shell
