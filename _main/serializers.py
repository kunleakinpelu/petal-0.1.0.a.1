# from rest_framework import serializers
#
# class PetalSerializer(serializers.Serializer):
#     id = serializers.SerializerMethodField()
#     type = serializers.SerializerMethodField()
#     created = serializers.DateTimeField(read_only=True)
#
#     def get_id(self, obj):
#         try:
#             return obj.object_uuid
#         except AttributeError:
#             return None
#
#     def get_type(self, obj):
#         return obj.__class__.__name__.lower()
#
#     def update(self, instance, validated_data):
#         task_param = {
#             "object_uuid": instance.object_uuid,
#             "label": instance.get_child_label().lower()
#         }
#         spawn_task(task_func=update_search_object, task_param=task_param)
#         return instance