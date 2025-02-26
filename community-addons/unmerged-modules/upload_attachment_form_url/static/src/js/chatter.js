/** @odoo-module */

import { _t } from "@web/core/l10n/translation";
import { patch } from "@web/core/utils/patch";
import { Chatter } from "@mail/chatter/web_portal/chatter";
import { UrlDialog } from "./url_dialog"
import { useService } from "@web/core/utils/hooks";

patch(Chatter.prototype, {
    setup() {
        super.setup();
        var self = this;
        this.dialog = useService("dialog");
        this.notification = useService("notification");
    },

    _onClickUrlAdd(e) {
        var self = this;
        self.dialog.add(UrlDialog, {
            uploadUrlImage: (data) => this.uploadUrlImage(data),
        });
    },

    async uploadUrlImage(data){
        var self = this;
        await self.uploadFile(data.base64,data.file_name,data.mime_type);
    },

    async uploadFile(data, filename, type) {
        var self = this;
        var def = await new Promise(function (resolve, reject) {
            if (data != undefined || data.length != 0) {                
                var binary = self.fixBinary(atob(data));                
                var blob = new Blob([binary], {type: type});
                var newFile = new File([blob],filename,{type:type});
                resolve(newFile);
                if (newFile) {
                    self.uploadFileToAttachmentBox(newFile);
                }
            } else {
                reject();
            }
        });
        return def;
    },

    fixBinary (data) {
        var self = this;
        var length = data.length;
        var buf = new ArrayBuffer(length);
        var arr = new Uint8Array(buf);
        for (var i = 0; i < length; i++) {
          arr[i] = data.charCodeAt(i);
        }
        return buf;
    },

    async uploadFileToAttachmentBox(file) {
        var self = this;
        if (!file) {
            return;
        }
        await self.attachmentUploader.uploadFile(file);
    }
});
