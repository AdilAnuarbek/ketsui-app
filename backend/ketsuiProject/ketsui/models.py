# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    def __str__(self):
        return self.title


# class Chr(models.Model):
#     entr = models.OneToOneField('Entr', models.DO_NOTHING, db_column='entr', primary_key=True)
#     chr = models.CharField(max_length=1)
#     bushu = models.SmallIntegerField(blank=True, null=True)
#     strokes = models.SmallIntegerField(blank=True, null=True)
#     freq = models.SmallIntegerField(blank=True, null=True)
#     grade = models.SmallIntegerField(blank=True, null=True)
#     jlpt = models.SmallIntegerField(blank=True, null=True)
#     radname = models.CharField(max_length=50, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'chr'
#         unique_together = (('entr', 'chr'),)
#
#
# class Cinf(models.Model):
#     pk = models.CompositePrimaryKey('entr', 'kw', 'value', 'mctype')
#     entr = models.ForeignKey(Chr, models.DO_NOTHING, db_column='entr')
#     kw = models.ForeignKey('Kwcinf', models.DO_NOTHING, db_column='kw')
#     value = models.CharField(max_length=50)
#     mctype = models.CharField(max_length=50)
#
#     class Meta:
#         managed = False
#         db_table = 'cinf'
#         unique_together = (('entr', 'kw', 'value', 'mctype'),)
#
#
# class Conj(models.Model):
#     id = models.SmallIntegerField(primary_key=True)
#     name = models.CharField(unique=True, max_length=50, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'conj'
#
#
# class Conjo(models.Model):
#     pk = models.CompositePrimaryKey('pos', 'conj', 'neg', 'fml', 'onum')
#     pos = models.ForeignKey('Kwpos', models.DO_NOTHING, db_column='pos')
#     conj = models.ForeignKey(Conj, models.DO_NOTHING, db_column='conj')
#     neg = models.BooleanField()
#     fml = models.BooleanField()
#     onum = models.SmallIntegerField()
#     stem = models.SmallIntegerField(blank=True, null=True)
#     okuri = models.CharField(max_length=50)
#     euphr = models.CharField(max_length=50, blank=True, null=True)
#     euphk = models.CharField(max_length=50, blank=True, null=True)
#     pos2 = models.ForeignKey('Kwpos', models.DO_NOTHING, db_column='pos2', related_name='conjo_pos2_set', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'conjo'
#         unique_together = (('pos', 'conj', 'neg', 'fml', 'onum'),)
#
#
# class ConjoNotes(models.Model):
#     pk = models.CompositePrimaryKey('pos', 'conj', 'neg', 'fml', 'onum', 'note')
#     pos = models.ForeignKey(Conjo, models.DO_NOTHING, db_column='pos')
#     conj = models.SmallIntegerField()
#     neg = models.BooleanField()
#     fml = models.BooleanField()
#     onum = models.SmallIntegerField()
#     note = models.ForeignKey('Conotes', models.DO_NOTHING, db_column='note')
#
#     class Meta:
#         managed = False
#         db_table = 'conjo_notes'
#         unique_together = (('pos', 'conj', 'neg', 'fml', 'onum', 'note'),)
#
#
# class Conotes(models.Model):
#     id = models.IntegerField(primary_key=True)
#     txt = models.TextField()
#
#     class Meta:
#         managed = False
#         db_table = 'conotes'
#
#
# class Db(models.Model):
#     id = models.IntegerField(primary_key=True)
#     active = models.BooleanField(blank=True, null=True)
#     ts = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'db'
#
#
# class Dial(models.Model):
#     pk = models.CompositePrimaryKey('entr', 'sens', 'kw')
#     entr = models.ForeignKey('Sens', models.DO_NOTHING, db_column='entr')
#     sens = models.IntegerField()
#     ord = models.SmallIntegerField()
#     kw = models.ForeignKey('Kwdial', models.DO_NOTHING, db_column='kw')
#
#     class Meta:
#         managed = False
#         db_table = 'dial'
#         unique_together = (('entr', 'sens', 'kw'),)


class Entr(models.Model):
    src = models.ForeignKey('Kwsrc', models.DO_NOTHING, db_column='src')
    stat = models.ForeignKey('Kwstat', models.DO_NOTHING, db_column='stat')
    seq = models.BigIntegerField()
    dfrm = models.OneToOneField('self', models.DO_NOTHING, db_column='dfrm', blank=True, null=True)
    unap = models.BooleanField()
    srcnote = models.CharField(max_length=255, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    idx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entr'
        unique_together = (('src', 'seq'),)


# class Entrsnd(models.Model):
#     pk = models.CompositePrimaryKey('entr', 'snd')
#     entr = models.ForeignKey(Entr, models.DO_NOTHING, db_column='entr')
#     ord = models.SmallIntegerField()
#     snd = models.ForeignKey('Snd', models.DO_NOTHING, db_column='snd')
#
#     class Meta:
#         managed = False
#         db_table = 'entrsnd'
#         unique_together = (('entr', 'snd'),)
#
#
# class Fld(models.Model):
#     pk = models.CompositePrimaryKey('entr', 'sens', 'kw')
#     entr = models.ForeignKey('Sens', models.DO_NOTHING, db_column='entr')
#     sens = models.SmallIntegerField()
#     ord = models.SmallIntegerField()
#     kw = models.ForeignKey('Kwfld', models.DO_NOTHING, db_column='kw')
#
#     class Meta:
#         managed = False
#         db_table = 'fld'
#         unique_together = (('entr', 'sens', 'kw'),)
#
#
# class Freq(models.Model):
#     entr = models.ForeignKey('Rdng', models.DO_NOTHING, db_column='entr')
#     rdng = models.SmallIntegerField(blank=True, null=True)
#     kanj = models.SmallIntegerField(blank=True, null=True)
#     kw = models.ForeignKey('Kwfreq', models.DO_NOTHING, db_column='kw')
#     value = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'freq'
#         unique_together = (('entr', 'kanj', 'kw', 'value'), ('entr', 'rdng', 'kw', 'value'),)


# class Gloss(models.Model):
#     pk = models.CompositePrimaryKey('entr', 'sens', 'gloss')
#     entr = models.ForeignKey('Sens', models.DO_NOTHING, db_column='entr')
#     sens = models.SmallIntegerField()
#     gloss = models.SmallIntegerField()
#     lang = models.ForeignKey('Kwlang', models.DO_NOTHING, db_column='lang')
#     ginf = models.ForeignKey('Kwginf', models.DO_NOTHING, db_column='ginf')
#     txt = models.CharField(max_length=2048)
#
#     class Meta:
#         managed = False
#         db_table = 'gloss'
#         unique_together = (('entr', 'sens', 'gloss'), ('entr', 'sens', 'lang', 'txt'),)


# class Grp(models.Model):
#     pk = models.CompositePrimaryKey('entr', 'kw')
#     entr = models.ForeignKey(Entr, models.DO_NOTHING, db_column='entr')
#     kw = models.ForeignKey('Kwgrp', models.DO_NOTHING, db_column='kw')
#     ord = models.IntegerField()
#     notes = models.CharField(max_length=250, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'grp'
#         unique_together = (('entr', 'kw'),)
#
#
# class Hist(models.Model):
#     pk = models.CompositePrimaryKey('entr', 'hist')
#     entr = models.ForeignKey(Entr, models.DO_NOTHING, db_column='entr')
#     hist = models.SmallIntegerField()
#     stat = models.ForeignKey('Kwstat', models.DO_NOTHING, db_column='stat')
#     unap = models.BooleanField()
#     dt = models.DateTimeField()
#     userid = models.CharField(max_length=20, blank=True, null=True)
#     name = models.CharField(max_length=60, blank=True, null=True)
#     email = models.CharField(max_length=120, blank=True, null=True)
#     diff = models.TextField(blank=True, null=True)
#     refs = models.TextField(blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#     eid = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'hist'
#         unique_together = (('entr', 'hist'),)


class Kanj(models.Model):
    pk = models.CompositePrimaryKey('entr', 'kanj')
    entr = models.ForeignKey(Entr, models.DO_NOTHING, db_column='entr')
    kanj = models.SmallIntegerField()
    txt = models.CharField(max_length=2048)

    class Meta:
        managed = False
        db_table = 'kanj'
        unique_together = (('entr', 'kanj'), ('entr', 'txt'),)


# class Kinf(models.Model):
#     pk = models.CompositePrimaryKey('entr', 'kanj', 'kw')
#     entr = models.ForeignKey(Kanj, models.DO_NOTHING, db_column='entr')
#     kanj = models.SmallIntegerField()
#     ord = models.SmallIntegerField()
#     kw = models.ForeignKey('Kwkinf', models.DO_NOTHING, db_column='kw')
#
#     class Meta:
#         managed = False
#         db_table = 'kinf'
#         unique_together = (('entr', 'kanj', 'kw'),)
#
#
# class Krslv(models.Model):
#     pk = models.CompositePrimaryKey('entr', 'kw', 'value')
#     entr = models.ForeignKey(Entr, models.DO_NOTHING, db_column='entr')
#     kw = models.SmallIntegerField()
#     value = models.CharField(max_length=50)
#
#     class Meta:
#         managed = False
#         db_table = 'krslv'
#         unique_together = (('entr', 'kw', 'value'),)
#
#
# class Kwcinf(models.Model):
#     id = models.SmallIntegerField(primary_key=True)
#     kw = models.CharField(unique=True, max_length=50)
#     descr = models.CharField(max_length=250, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'kwcinf'
#
#
# class Kwdial(models.Model):
#     id = models.SmallIntegerField(primary_key=True)
#     kw = models.CharField(unique=True, max_length=20)
#     descr = models.CharField(max_length=255, blank=True, null=True)
#     ents = models.JSONField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'kwdial'
#
#
# class Kwfld(models.Model):
#     id = models.SmallIntegerField(primary_key=True)
#     kw = models.CharField(unique=True, max_length=20)
#     descr = models.CharField(max_length=255, blank=True, null=True)
#     ents = models.JSONField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'kwfld'
#
#
# class Kwfreq(models.Model):
#     id = models.SmallIntegerField(primary_key=True)
#     kw = models.CharField(unique=True, max_length=20)
#     descr = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'kwfreq'
#
#
# class Kwginf(models.Model):
#     id = models.SmallIntegerField(primary_key=True)
#     kw = models.CharField(unique=True, max_length=20)
#     descr = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'kwginf'
#
#
# class Kwgrp(models.Model):
#     kw = models.CharField(unique=True, max_length=20)
#     descr = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'kwgrp'
#
#
# class Kwkinf(models.Model):
#     id = models.SmallIntegerField(primary_key=True)
#     kw = models.CharField(max_length=20)
#     descr = models.CharField(max_length=255, blank=True, null=True)
#     ents = models.JSONField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'kwkinf'
#
#
# class Kwlang(models.Model):
#     id = models.SmallIntegerField(primary_key=True)
#     kw = models.CharField(unique=True, max_length=20)
#     descr = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'kwlang'
#
#
# class Kwmisc(models.Model):
#     id = models.SmallIntegerField(primary_key=True)
#     kw = models.CharField(max_length=20)
#     descr = models.CharField(max_length=255, blank=True, null=True)
#     ents = models.JSONField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'kwmisc'
#
#
# class Kwpos(models.Model):
#     id = models.SmallIntegerField(primary_key=True)
#     kw = models.CharField(unique=True, max_length=20)
#     descr = models.CharField(max_length=255, blank=True, null=True)
#     ents = models.JSONField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'kwpos'
#
#
# class Kwrinf(models.Model):
#     id = models.SmallIntegerField(primary_key=True)
#     kw = models.CharField(unique=True, max_length=20)
#     descr = models.CharField(max_length=255, blank=True, null=True)
#     ents = models.JSONField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'kwrinf'
#
#
class Kwsrc(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    kw = models.CharField(unique=True, max_length=20)
    descr = models.CharField(max_length=255, blank=True, null=True)
    dt = models.DateField(blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    seq = models.CharField(max_length=20)
    sinc = models.SmallIntegerField(blank=True, null=True)
    smin = models.BigIntegerField(blank=True, null=True)
    smax = models.BigIntegerField(blank=True, null=True)
    srct = models.ForeignKey('Kwsrct', models.DO_NOTHING, db_column='srct', to_field='kw')

    class Meta:
        managed = False
        db_table = 'kwsrc'


class Kwsrct(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    kw = models.CharField(unique=True, max_length=20)
    descr = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kwsrct'


class Kwstat(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    kw = models.CharField(unique=True, max_length=20)
    descr = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kwstat'
#
#
# class Kwxref(models.Model):
#     id = models.SmallIntegerField(primary_key=True)
#     kw = models.CharField(unique=True, max_length=20)
#     descr = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'kwxref'
#
#
# class Lsrc(models.Model):
#     pk = models.CompositePrimaryKey('entr', 'sens', 'lang', 'txt')
#     entr = models.ForeignKey('Sens', models.DO_NOTHING, db_column='entr')
#     sens = models.SmallIntegerField()
#     ord = models.SmallIntegerField()
#     lang = models.ForeignKey(Kwlang, models.DO_NOTHING, db_column='lang')
#     txt = models.CharField(max_length=250)
#     part = models.BooleanField(blank=True, null=True)
#     wasei = models.BooleanField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'lsrc'
#         unique_together = (('entr', 'sens', 'lang', 'txt'),)
#
#
# class Misc(models.Model):
#     pk = models.CompositePrimaryKey('entr', 'sens', 'kw')
#     entr = models.ForeignKey('Sens', models.DO_NOTHING, db_column='entr')
#     sens = models.SmallIntegerField()
#     ord = models.SmallIntegerField()
#     kw = models.ForeignKey(Kwmisc, models.DO_NOTHING, db_column='kw')
#
#     class Meta:
#         managed = False
#         db_table = 'misc'
#         unique_together = (('entr', 'sens', 'kw'),)
#
#
# class Pos(models.Model):
#     pk = models.CompositePrimaryKey('entr', 'sens', 'kw')
#     entr = models.ForeignKey('Sens', models.DO_NOTHING, db_column='entr')
#     sens = models.SmallIntegerField()
#     ord = models.SmallIntegerField()
#     kw = models.ForeignKey(Kwpos, models.DO_NOTHING, db_column='kw')
#
#     class Meta:
#         managed = False
#         db_table = 'pos'
#         unique_together = (('entr', 'sens', 'kw'),)
#
#
# class Rad(models.Model):
#     pk = models.CompositePrimaryKey('num', 'var')
#     num = models.SmallIntegerField()
#     var = models.SmallIntegerField()
#     rchr = models.CharField(max_length=1, blank=True, null=True)
#     chr = models.CharField(max_length=1, blank=True, null=True)
#     strokes = models.SmallIntegerField(blank=True, null=True)
#     loc = models.CharField(max_length=1, blank=True, null=True)
#     name = models.CharField(max_length=50, blank=True, null=True)
#     examples = models.CharField(max_length=20, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'rad'
#         unique_together = (('num', 'var'),)
#
#
# class Rdng(models.Model):
#     pk = models.CompositePrimaryKey('entr', 'rdng')
#     entr = models.ForeignKey(Entr, models.DO_NOTHING, db_column='entr')
#     rdng = models.SmallIntegerField()
#     txt = models.CharField(max_length=2048)
#
#     class Meta:
#         managed = False
#         db_table = 'rdng'
#         unique_together = (('entr', 'rdng'), ('entr', 'txt'),)
#
#
# class Rdngsnd(models.Model):
#     pk = models.CompositePrimaryKey('entr', 'rdng', 'snd')
#     entr = models.ForeignKey(Rdng, models.DO_NOTHING, db_column='entr')
#     rdng = models.IntegerField()
#     ord = models.SmallIntegerField()
#     snd = models.ForeignKey('Snd', models.DO_NOTHING, db_column='snd')
#
#     class Meta:
#         managed = False
#         db_table = 'rdngsnd'
#         unique_together = (('entr', 'rdng', 'snd'),)
#
#
# class Restr(models.Model):
#     pk = models.CompositePrimaryKey('entr', 'rdng', 'kanj')
#     entr = models.ForeignKey(Rdng, models.DO_NOTHING, db_column='entr')
#     rdng = models.SmallIntegerField()
#     kanj = models.SmallIntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'restr'
#         unique_together = (('entr', 'rdng', 'kanj'),)
#
#
# class Rinf(models.Model):
#     pk = models.CompositePrimaryKey('entr', 'rdng', 'kw')
#     entr = models.ForeignKey(Rdng, models.DO_NOTHING, db_column='entr')
#     rdng = models.SmallIntegerField()
#     ord = models.SmallIntegerField()
#     kw = models.ForeignKey(Kwrinf, models.DO_NOTHING, db_column='kw')
#
#     class Meta:
#         managed = False
#         db_table = 'rinf'
#         unique_together = (('entr', 'rdng', 'kw'),)
#
#
# class Sens(models.Model):
#     pk = models.CompositePrimaryKey('entr', 'sens')
#     entr = models.ForeignKey(Entr, models.DO_NOTHING, db_column='entr')
#     sens = models.SmallIntegerField()
#     notes = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'sens'
#         unique_together = (('entr', 'sens'),)
#
#
# class Snd(models.Model):
#     file = models.ForeignKey('Sndfile', models.DO_NOTHING, db_column='file')
#     strt = models.IntegerField()
#     leng = models.IntegerField()
#     trns = models.TextField(blank=True, null=True)
#     notes = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'snd'
#
#
# class Sndfile(models.Model):
#     vol = models.ForeignKey('Sndvol', models.DO_NOTHING, db_column='vol')
#     title = models.CharField(max_length=50, blank=True, null=True)
#     loc = models.CharField(max_length=500, blank=True, null=True)
#     type = models.SmallIntegerField(blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'sndfile'
#
#
# class Sndvol(models.Model):
#     title = models.CharField(max_length=50, blank=True, null=True)
#     loc = models.CharField(max_length=500, blank=True, null=True)
#     type = models.SmallIntegerField()
#     idstr = models.CharField(max_length=100, blank=True, null=True)
#     corp = models.ForeignKey(Kwsrc, models.DO_NOTHING, db_column='corp', blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'sndvol'
#
#
# class Stagk(models.Model):
#     pk = models.CompositePrimaryKey('entr', 'sens', 'kanj')
#     entr = models.ForeignKey(Sens, models.DO_NOTHING, db_column='entr')
#     sens = models.SmallIntegerField()
#     kanj = models.SmallIntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'stagk'
#         unique_together = (('entr', 'sens', 'kanj'),)
#
#
# class Stagr(models.Model):
#     pk = models.CompositePrimaryKey('entr', 'sens', 'rdng')
#     entr = models.ForeignKey(Sens, models.DO_NOTHING, db_column='entr')
#     sens = models.SmallIntegerField()
#     rdng = models.SmallIntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'stagr'
#         unique_together = (('entr', 'sens', 'rdng'),)
#
#
# class Xref(models.Model):
#     pk = models.CompositePrimaryKey('entr', 'sens', 'xref', 'xentr', 'xsens')
#     entr = models.ForeignKey(Sens, models.DO_NOTHING, db_column='entr')
#     sens = models.SmallIntegerField()
#     xref = models.SmallIntegerField()
#     typ = models.ForeignKey(Kwxref, models.DO_NOTHING, db_column='typ')
#     xentr = models.ForeignKey(Sens, models.DO_NOTHING, db_column='xentr', related_name='xref_xentr_set')
#     xsens = models.SmallIntegerField()
#     rdng = models.SmallIntegerField(blank=True, null=True)
#     kanj = models.SmallIntegerField(blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#     nosens = models.BooleanField()
#     lowpri = models.BooleanField()
#
#     class Meta:
#         managed = False
#         db_table = 'xref'
#         unique_together = (('entr', 'sens', 'xref', 'xentr', 'xsens'),)
#
#
# class Xresolv(models.Model):
#     pk = models.CompositePrimaryKey('entr', 'sens', 'typ', 'ord')
#     entr = models.ForeignKey(Sens, models.DO_NOTHING, db_column='entr')
#     sens = models.SmallIntegerField()
#     ord = models.SmallIntegerField()
#     typ = models.ForeignKey(Kwxref, models.DO_NOTHING, db_column='typ')
#     rtxt = models.CharField(max_length=250, blank=True, null=True)
#     ktxt = models.CharField(max_length=250, blank=True, null=True)
#     tsens = models.SmallIntegerField(blank=True, null=True)
#     vsrc = models.SmallIntegerField(blank=True, null=True)
#     vseq = models.BigIntegerField(blank=True, null=True)
#     notes = models.CharField(max_length=250, blank=True, null=True)
#     prio = models.BooleanField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'xresolv'
#         unique_together = (('entr', 'sens', 'typ', 'ord'),)
