import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {
    width: 1080
    height: 960
    visible: true
    title: "Gestion de stock"

    RowLayout{
        Image {
            source: "../images/odoo_inventory_app.png"
            width:40
            height:40
            sourceSize.width:40
            sourceSize.height:40
            fillMode: Image.PreserveAspectFit
            clip: true
        }

        MenuBar{
            background: Rectangle{
                color: "#FFFFFF"
            }
            Menu{
                title:"Operation"
                MenuItem{
                    text:"Transfert"
                }
                MenuItem{
                    text:"Replenishment"
                }
            }
            Menu{
                title:"Product"
                MenuItem{
                    text:"Product"
                }
                MenuItem{
                    text:"Product variant"
                }
            }
            Menu{
                title:"Reporting"
                MenuItem{
                    text:"Stock"
                }
                MenuItem{
                    text:"Location"
                }
            }
            Menu{
                title:"Configuration"
                MenuItem{
                    text:"Vendor"
                }
                MenuItem{
                    text:"Location"
                }
            }
        }

    }
    

}