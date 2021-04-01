# Самоконтроль выполненения задания

1. Где расположен файл с `some_fact` из второго пункта задания? 
   - in the file site.yml, playbook/site.yml
2. Какая команда нужна для запуска вашего `playbook` на окружении `test.yml`?
   - ansible-playbook site.yml -i inventory/test.yml
3. Какой командой можно зашифровать файл?
   - ansible-vault create <filename>
4. Какой командой можно расшифровать файл?
   - ansible-vault decrypt <filename>
5. Можно ли посмотреть содержимое зашифрованного файла без команды расшифровки файла? Если можно, то как?
   - ansible-vault view <filename>
6. Как выглядит команда запуска `playbook`, если переменные зашифрованы?
   - ansible-playbook myplaybook.yml --ask-vault-pass
7. Как называется модуль подключения к host на windows?
   - winrm
8. Приведите полный текст команды для поиска информации в документации ansible для модуля подключений ssh
   - ansible-doc -t connection ssh
9. Какой параметр из модуля подключения `ssh` необходим для того, чтобы определить пользователя, под которым необходимо совершать подключение?
   - ansible_user=root (inventory file with 
[all:vars]
ansible_connection=ssh
ansible_user=vagrant
ansible_ssh_pass=vagrant)
