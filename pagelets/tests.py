from django.test import TestCase, Client
from django.template import compile_string, TemplateSyntaxError, StringOrigin
from django.template.context import Context
from django.contrib.auth.models import User, Permission
from django.core.urlresolvers import reverse

from pagelets.models import Page, Pagelet

class PageletsTest(TestCase):
    def setUp(self):
        self.editor = User.objects.create_user(
            username='editor',
            email='editor@example.com',
            password='abc123',
        )
        change_pagelet = Permission.objects.get(
            codename='change_pagelet', 
            content_type__app_label='pagelets', 
            content_type__model='pagelet',
        )
        add_pagelet = Permission.objects.get(
            codename='add_pagelet', 
            content_type__app_label='pagelets', 
            content_type__model='pagelet',
        )
        self.editor.user_permissions.add(change_pagelet)
        self.editor.user_permissions.add(add_pagelet)
        self.c = Client()
        
    def testViewNonexistentPagelet(self):
        template_str = """{% spaceless %}
{% load pagelet_tags %}
{% render_pagelet 'nonexistent-pagelet' %}        
{% endspaceless %}"""
        origin = StringOrigin('test')
        compiled = compile_string(template_str, origin).render(Context())
        self.assertEqual(compiled, '<div class="pagelet nonexistent-pagelet"><div class="pagelet-content"></div></div>')
    
    def testCreateNotexistentPagelet(self):
        self.c.login(username=self.editor.username, password='abc123')
        url = reverse('create_pagelet', kwargs={'pagelet_slug': 'new-pagelet'})
        response = self.c.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Pagelet.objects.count(), 1)
        pagelet = Pagelet.objects.get()
        url = reverse('edit_pagelet', kwargs={'pagelet_id': pagelet.id})
        self.assertRedirects(response, url)
    
    def testEditPagelet(self):
        self.c.login(username=self.editor.username, password='abc123')
        pagelet = Pagelet.objects.create(
            created_by=self.editor, 
            modified_by=self.editor,
        )
        url = reverse('edit_pagelet', kwargs={'pagelet_id': pagelet.real.pk})
        response = self.c.get(url)
        self.assertEqual(response.status_code, 200)
        data = {
            'type': 'html',
            'content': '<p>new content</p>',
        }
        response = self.c.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, data['content'])
        self.assertContains(response, 'Preview pagelet #%s' % pagelet.id)
        data['save_btn'] = 'Save'
        response = self.c.post(url + '?next=/', data)
        self.assertEqual(302, response.status_code)
        pagelet = Pagelet.objects.get(pk=pagelet.id)
        self.assertEqual(pagelet.content, data['content'])
        
    def testViewPage(self):
        page = Page.objects.create(
            title='New Page', 
            slug='new-page', 
            created_by=self.editor, 
            modified_by=self.editor,
        )
        pagelet = page.inline_pagelets.create(
            content='<p>main content</p>',
            css_classes='main',
            created_by=self.editor, 
            modified_by=self.editor,
        )
        url = reverse('view_page', kwargs={'page_slug': page.slug})
        response = self.c.get(url)
        self.assertContains(response, pagelet.content)

