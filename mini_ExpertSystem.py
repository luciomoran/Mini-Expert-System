from experta import *


class DeployQuestion(Fact):
    pass


class cloudPlatform(KnowledgeEngine):
    @Rule(DeployQuestion(app_size="small",
                         app_type=L("Rails") | L("Node") | L("Laravel"),
                         app_require_specific_infrastructure="no",
                         have_enough_money="no",
                         know_about_infrastructure="no",
                         will_you_app_grown_up_soon="no",
                         part_of_a_big_companie="no",
                         want_a_vpn="no",
                         app_needs_specific_libraries="no",
                         free_version_option="no"
                         ))

    def you_better_use_heroku(self):
        print("Choose Heroku!")


    @Rule(DeployQuestion(app_size=L("medium") | L("big"),
                         app_type=L("Rails") | L("Node") | L("Laravel") | L("None"),
                         app_require_specific_infrastructure="yes",
                         have_enough_money=L("no") | L("yes"),
                         know_about_infrastructure="yes",
                         will_you_app_grown_up_soon=L("no") | L("yes"),
                         part_of_a_big_companie=L("no") | L("yes"),
                         want_a_vpn=L("no") | L("yes"),
                         app_needs_specific_libraries=L("no") | "yes",
                         free_version_option=L("no") | L("yes")
                         ))
    
    def you_better_use_aws(self):
        print("Choose the Amazon Web Services!")


    @Rule(DeployQuestion(app_size=L("medium") | L("big"),
                         app_type=L("Rails") | L("Node") | L("Laravel") | L("None"),
                         app_require_specific_infrastructure=L("yes") | L("no"),
                         have_enough_money=L("no") | L("yes"),
                         know_about_infrastructure=L("yes") | L("no"),
                         will_you_app_grown_up_soon=L("no") | L("yes"),
                         part_of_a_big_companie=L("no") | L("yes"),
                         want_a_vpn=L("no") | L("yes"),
                         app_needs_specific_libraries=L("no") | "yes",
                         free_version_option=L("no") | L("yes")
                         ))

    def you_better_use_google(self):
        print("Choose Google Cloud!")


app_size = input("Your app is small, medium or big?" )
app_type = input("Your app uses Rails, Node or something like these?" )
app_require_specific_infrastructure = input("Your app uses a specific infrastructure? ")
have_enough_money = input("Do you have enough money for your app? ")
know_about_infrastructure = input("Do you know about infrastructures: ")
will_you_app_grown_up_soon = input("Will your app exponentially grown up soon? ")
part_of_a_big_companie = input("Does your app it's part of one of the biggest companies around the world ")
want_a_vpn = input("Do you need a VPN? ")
app_needs_specific_libraries = input("Does your app need specific libraries ")
free_version_option = input("Does your app will have a free version? ")

engine = cloudPlatform()
engine.reset()
engine.declare(DeployQuestion(app_size=app_size, app_type=app_type, app_require_specific_infrastructure=app_require_specific_infrastructure,
                              have_enough_money=have_enough_money, know_about_infrastructure=know_about_infrastructure,
                              will_you_app_grown_up_soon = will_you_app_grown_up_soon, part_of_a_big_companie = part_of_a_big_companie,
                              want_a_vpn=want_a_vpn, app_needs_specific_libraries = app_needs_specific_libraries,
                              free_version_option = free_version_option))

engine.run()