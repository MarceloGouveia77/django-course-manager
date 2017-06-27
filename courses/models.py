from django.db import models

class CourseManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | \
            models.Q(description__icontains=query)
        ) #CONSULTA OR

class Course(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição', blank=True) #Campo não obrigatório
    about = models.TextField('Sobre o curso', blank=True)
    start_date = models.DateField(
        'Data de Inicio', null=True, blank=True #NULL a nível de banco de dados
    )
    image = models.ImageField(
        upload_to='courses/images', verbose_name='Imagem',
        null=True, blank=True)

    created_at = models.DateTimeField(
        'Criado em', auto_now_add = True #Toda vez q colocar um curso, add essa variável
    )
    updated_at = models.DateTimeField(
        'Atualizado em', auto_now=True #Toda vez q for salvo, altera update_at
    )

    objects = CourseManager() # SUBSTITUI A FUNÇÃO OBJECTS PADRÃO

    def __str__(self):
        return self.name
    
    @models.permalink
    def get_absolute_url(self):
        return ('courses:details', (), {'slug': self.slug})

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['name']